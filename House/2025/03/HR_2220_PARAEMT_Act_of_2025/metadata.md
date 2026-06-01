# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2220?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2220
- Title: PARA–EMT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2220
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-05-20T08:08:42Z
- Update date including text: 2026-05-20T08:08:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2220",
    "number": "2220",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "PARA\u2013EMT Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:42Z",
    "updateDateIncludingText": "2026-05-20T08:08:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-03-18T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-18T16:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MN"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "OR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NM"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "OR"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "WA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "OR"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "WA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "ME"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "PA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "VA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "VA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2220ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2220\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Ms. Perez (for herself, Mr. Finstad , Mr. Feenstra , Ms. Bonamici , Mr. Lawler , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo preserve access to emergency medical services.\n#### 1. Short title\nThis Act may be cited as the Preserve Access to Rapid Ambulance Emergency Medical Treatment Act of 2025 or the PARA\u2013EMT Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nParamedics and emergency medical technicians (in this section referred to as EMTs ) provide care to ill or injured people in emergency medical settings and are a vital component of the Nation\u2019s Emergency Medical Services (in this section referred to as EMS ) system.\n**(2)**\nEMTs provide basic emergency medical care and transportation for patients while paramedics provide advanced emergency medical care such as intubation, oral and intravenous drug administration, and other procedures.\n**(3)**\nThe United States EMS system is facing a crippling workforce shortage, a long-term problem that has been building for more than a decade.\n**(4)**\nIn 2019, the Health Resources and Services Administration reported that by 2030, there would be a need for an additional 42,000 EMTs and Paramedics to meet the nation\u2019s demand for healthcare services.\n**(5)**\nThe COVID\u201319 pandemic has further exacerbated this workforce shortage, with ambulance crews suffering the effects of surging demand, burnout, fear of illness and stress on their families.\n**(6)**\nA 2021 survey of nearly 20,000 employees working at 258 EMS organizations found that overall turnover among paramedics and EMTs ranges from 20 to 30 percent annually.\n**(7)**\nWith COVID\u201319 halting clinical and in-person trainings for a significant period of time, the pipeline of new EMS staff has been stretched even thinner.\n#### 3. EMS preparedness and response workforce shortage pilot program\nTitle XII of the Public Health Service Act ( 42 U.S.C. 300d et seq. ) is amended by inserting after section 1204 the following:\n1205. EMS preparedness and response workforce shortage pilot program (a) Grants The Secretary, acting through the Assistant Secretary for Preparedness and Response, shall establish a pilot program to award grants to eligible emergency medical services agencies to support the recruitment and training of emergency medical technicians and paramedics to improve access to, and enhance the quality of, emergency medical services. (b) Application An eligible emergency medical services agency seeking a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (c) Use of funds An eligible emergency medical services agency receiving a grant under this section shall use funds received through the grant to implement a new program or enhance an existing program to\u2014 (1) recruit and retain emergency medical services personnel, which may include volunteer personnel; (2) train emergency medical services personnel to obtain and maintain licenses and certifications relevant to service in an emergency medical services agency; (3) conduct courses and implement apprenticeship programs that qualify graduates to serve in an emergency medical services agency in accordance with State and local requirements; (4) fund specific training to meet Federal or State licensing or certification requirements; (5) develop new ways to educate emergency medical services personnel through the use of technology-enhanced educational methods; (6) establish wellness and fitness programs for emergency medical services personnel to ensure that such personnel are able to carry out their duties, including programs dedicated to raising awareness of, and prevention of, job-related mental health issues; or (7) train emergency medical services personnel to care for people with mental and substance use disorders in emergency situations. (d) Prioritization In awarding grants under this section, the Secretary shall prioritize eligible emergency medical services agencies that\u2014 (1) emphasize the recruitment and training of youth, particularly high school students, rural youth, and youth from low-income or disadvantaged backgrounds; (2) develop and implement programs to assist veterans who completed military emergency medical technician training while serving in the Armed Forces of the United States to meet certification, licensure, and other requirements applicable to becoming an emergency medical technician or paramedic; (3) are small or are located in rural areas and serve rural populations; or (4) address such other priorities as the Secretary considers appropriate. (e) Allocation of grants to rural emergency medical services agencies The Secretary shall ensure that not less than 20 percent of the total number of grants under this section are made to emergency medical services agencies located in rural areas. (f) Maximum grant amount The amount of a grant made under this section to a single grant recipient shall not exceed $1,000,000. (g) Reports (1) Report to Secretary An eligible emergency medical services agency receiving a grant under subsection (a) shall periodically submit to the Secretary a report evaluating the activities supported by the grant. (2) Report to public The Secretary shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate, and make publicly available, a report on the Secretary\u2019s findings with respect to the success of the program under this section in improving access to, and enhancing the quality of, emergency medical services. (h) Definition In this section, the term eligible emergency medical services agency means an entity that is\u2014 (1) licensed to deliver medical care outside of a medical facility under emergency conditions that occur as a result of the condition of the patient; and (2) delivers services (either on a compensated or volunteer basis) by an emergency medical services provider or other provider that is licensed or certified by the State involved as an emergency medical technician, a paramedic, or an equivalent professional (as determined by the State). (i) Authorization of appropriations (1) In general To carry out this section, there are authorized to be appropriated $50,000,000 for each of fiscal years 2026 through 2030. (2) Administrative costs The Secretary may use not more than 10 percent of the amount appropriated pursuant to paragraph (1) for a fiscal year for the administrative expenses of carrying out this section. .\n#### 4. Assisting veterans with military emergency medical training to meet requirements for becoming emergency medical technicians and civilian paramedics\nPart B of title III of the Public Health Service Act ( 42 U.S.C. 243 et seq. ) is amended by inserting after section 320B ( 42 U.S.C. 247d\u201311 ) the following:\n320C. Assisting veterans with military emergency medical training to meet requirements for becoming emergency medical technicians and civilian paramedics (a) Program The Secretary shall\u2014 (1) establish a program consisting of awarding demonstration grants to States to cover transition costs in order to assist veterans who completed robust military emergency medical technician or paramedic training while serving in the Armed Forces of the United States to meet certification, licensure, and other requirements applicable to becoming a civilian emergency medical technician or paramedic in the State; and (2) in implementing such program, assist States in honoring the service of such veterans who have completed training through such service in the Armed Forces of the United States and passed the respective National Registry of Emergency Medical Technicians exam to ease the transition to the civilian Nation\u2019s Emergency Medical Services workforce. (b) Use of funds A State receiving a grant under this section shall use amounts of such grants to prepare and implement a plan to assist with the transition of a veteran to becoming a civilian emergency medical technician or paramedic as described in subsection (a), including by establishing a grant program within the applicable State agency responsible for emergency medical services to cover\u2014 (1) the costs of training, education, certification, and credentialing by an accredited institution; and (2) fees for national testing for official certification and State fees to acquire State licensure. (c) Report The Secretary shall submit to the Congress an annual report on the program under this section. (d) Authorization of appropriations To carry out this section, there are authorized to be appropriated $20,000,000 for each of fiscal years 2026 through 2030. .\n#### 5. Study and report on emergency medical technician and paramedic workforce shortage\n##### (a) Study\nThe Secretary of Labor, in coordination with the Secretary of Health and Human Services, shall conduct a study on\u2014\n**(1)**\nthe number of currently available emergency medical technician and paramedic jobs, categorized by type of employer (such as ambulance services, local governments other than hospitals, and hospitals);\n**(2)**\nthe projected increase in available emergency medical technician and paramedic jobs from 2025 through 2034, categorized by type of employer;\n**(3)**\nthe percentage of available emergency medical technician and paramedic jobs from 2025 through 2034 that are expected to result from the need to replace workers who transfer to different occupations or exit the labor force;\n**(4)**\nthe availability of appropriate training and education programs in the United States sufficient to meet the projected demand for emergency medical technician and paramedic jobs from 2025 through 2034; and\n**(5)**\nthe projected shortage of emergency medical technicians and paramedics from 2025 through 2034.\n##### (b) Report to congress\nNot later than one year after the date of the enactment of this Act, the Secretary of Labor, in coordination with the Secretary of Health and Human Services, shall submit to Congress a report on the study conducted under subsection (a) together with such recommendations that the Secretaries determine are appropriate to address the projected shortage of emergency medical technicians and paramedics, including whether Schedule A should be expanded to include these occupations.",
      "versionDate": "2025-03-18",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-04T17:00:31Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2220ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "PARA\u2013EMT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PARA\u2013EMT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T07:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preserve Access to Rapid Ambulance Emergency Medical Treatment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T07:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To preserve access to emergency medical services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T07:18:30Z"
    }
  ]
}
```
