chimport os
import webbrowser
print('Do you want to raise a cherry pick PR?')
answer = int(input('1 - Yes \n2 - No \n'))
cherry_pick_list=[]
if answer==1:
  user_id=input('Enter cec id \n')
  id_list = int(input('How many commit Ids are there?'))
  for i in range(id_list):
    cherry_pick_id = input('Enter commit ID \n')
    cherry_pick_list.append(cherry_pick_id)
  branch_name = input('Enter branch name \n')
  commit_message = input('Enter commit message \n')
  add_all_messages = commit_message.split(' ')
  commit_message = '-'.join(add_all_messages)
  fix_or_feature = int(input('1 - Feature \n2 - fix \n'))
  branch_id = branch_name.split('/')
  full_path =input('Enter the complete path of the repo. For example: To run the code in the repo: cx-cloud-ui, use the TAB autocomplete to get the full path till /cx-cloud-ui \n')
  commands = []
  commands.append('cd /')
  commands.append('cd '+full_path)
  commands.append('git checkout ' + branch_name)
  commands.append('git pull')
  final_branch = ''
  if fix_or_feature ==1:
    try:
      final_branch = user_id+'/'+branch_id[1]+'/feat/' + commit_message
    except:
      final_branch = user_id+'/'+branch_id[0]+'/feat/' + commit_message
  else:
    try:
      final_branch = user_id+'/'+branch_id[1]+'/fix/' + commit_message
    except:
      final_branch = user_id+'/'+branch_id[0]+'/fix/' + commit_message

  commands.append('git checkout ' + final_branch)
  for number_of_commands in commands:
    os.system(number_of_commands)
  for cherry_pick_id in cherry_pick_list:
    try:
      cherry_pick=[]
      cherry_pick.append('git cherry-pick '+cherry_pick_id)
      os.system(cherry_pick)
    except:
      ans=int(input('Resolve merge conflicts. Once done, press 1 '))
      if ans==1:
        os.system('git add .')
        os.system("git commit -m 'resolved merge conflicts'")
        os.system('git cherry-pick '+cherry_pick_id)

  commands.append('git push -u origin '+ final_branch)
  webbrowser.open('https://github.com/CXEPI/cx-cloud-ui/pull/new/'+final_branch)
else:
  print('Why trigger this then????' + '\U0001F612')