# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5575
- Title: FASTER Act
- Congress: 119
- Bill type: HR
- Bill number: 5575
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-01-09T09:07:03Z
- Update date including text: 2026-01-09T09:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5575",
    "number": "5575",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000462",
        "district": "22",
        "firstName": "Lois",
        "fullName": "Rep. Frankel, Lois [D-FL-22]",
        "lastName": "Frankel",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "FASTER Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:07:03Z",
    "updateDateIncludingText": "2026-01-09T09:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "AZ"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "RI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "DC"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MD"
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
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5575ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5575\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Ms. Lois Frankel of Florida (for herself, Mr. Ciscomani , Mr. Magaziner , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo authorize grants to fire departments to conduct activities with the goals of reducing falls among older adults and reducing response time when responding to in-home emergencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Firefighters Assisting Seniors To Emergency Response Act or the FASTER Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the Centers for Disease Control and Prevention (CDC), about 14,000,000 falls are reported each year nationwide among adults age 65 and over.\n**(2)**\nThese falls result in 38,000 deaths.\n**(3)**\nEach year, approximately 3,000,000 older adults are treated in emergency departments for a fall injury.\n**(4)**\nFalls are the top cause of injury and injury-related deaths for adults over 65.\n**(5)**\nFalls among adults aged 65 and above result in over $80,000,000,000 per year in medical expenses.\n**(6)**\nMore than 95 percent of hip fractures are caused by falling.\n**(7)**\nFalls are the most common cause of traumatic brain injuries.\n**(8)**\nAccording to the National Institutes of Health (NIH), over 70 percent of falls occur in the home.\n**(9)**\nFalls can often be prevented, including by implementing simple home modifications.\n**(10)**\nFire department personnel can play an important role in preventing and responding to falls.\n#### 3. Firefighters assisting seniors to emergency response\n##### (a) Fall prevention and home safety grants\n**(1) In general**\nThe Administrator of FEMA shall make grants directly to career fire departments, combination fire departments, and volunteer fire departments for the purpose of implementing programs to improve home safety and prevent falls for older adults, including through fall prevention programs.\n**(2) Period of performance**\nGrants made under this subsection shall be for three years.\n**(3) Consideration**\nIn awarding grants under this subsection, the Administrator of FEMA may give preferential consideration to applications that involve non-Federal contributions that exceed the difference between 100 percent and the maximum percentage allowable Federal contribution specified in paragraph (5) for a year.\n**(4) Technical assistance**\nThe Administrator of FEMA may provide technical assistance to States, units of local government, Tribal governments, and other public entities in furtherance of the purposes of this section.\n**(5) Limitation on costs**\nThe portion of the costs of implementing programs to improve home safety and prevent falls for older adults provided by a grant under this paragraph may not exceed the following:\n**(A)**\nSeventy-five percent in the first year of such grant.\n**(B)**\nSeventy-five percent in the second year of such grant.\n**(C)**\nThirty-five percent in the third year of such grant.\n**(6) Administration**\nGrants made pursuant to this subsection shall be awarded on a competitive basis through a neutral peer review process.\n##### (b) Applications\n**(1) Restriction**\nNo grant may be made under this section unless an application has been submitted to, and approved by, the Administrator of FEMA.\n**(2) Form**\nAn application for a grant under this section shall be submitted to the Administrator of FEMA in such form, and containing such information, as the Administrator of FEMA may prescribe.\n**(3) Contents**\nAt a minimum, each application for a grant under this section shall\u2014\n**(A)**\nexplain the applicant\u2019s inability or challenges to implement without Federal assistance a program to improve home safety and prevent falls for older adults; and\n**(B)**\nspecify long-term plans for continuing such a program following the conclusion of Federal support provided under this section.\n##### (c) Allowable use of funds\nGrants under this section shall be used for any of the following purposes:\n**(1)**\nProcurement and installation of devices, including lock boxes, that can be installed on homes in order to allow emergency responders quicker access to a home in case of an emergency.\n**(2)**\nRecruitment, retention, salaries, and benefits of community paramedicine personnel, including firefighters, paramedics, EMTs, social workers, case managers, administrators, or other professionals for the purpose described in subsection (a)(1).\n**(3)**\nInstallation and replacement of smoke detectors and batteries.\n**(4)**\nCompilation of health information to permit emergency responders ready access to vital health data in case of an emergency.\n**(5)**\nMinor home modifications to reduce fall risks, including the following:\n**(A)**\nFlattening of rugs.\n**(B)**\nRemoval of tripping hazards.\n**(C)**\nInstallation of hand rails and grab bars, including supplies, labor, and insurance.\n**(6)**\nRisk assessment and reconciliation of medications.\n**(7)**\nReferral to classes, medical professionals, and other community resources that educate seniors on reducing fall risks.\n##### (d) Rules regarding use of funds\n**(1) Limitation**\nFunds made available under this section to fire departments may not be used to supplant State or local funds, or, in the case of Tribal governments, funds supplied by the Bureau of Indian Affairs, but shall be used to increase the amount of funds that would, in the absence of Federal funds received under this section, be made available from State or local sources, or in the case of Tribal governments, from funds supplied by the Bureau of Indian Affairs.\n**(2) Relating to prior reductions**\nNo grant shall be awarded pursuant to this section to a municipality or other recipient whose annual budget at the time of the application for fire-related programs and emergency response has been reduced below 80 percent of the average funding level in the three years immediately preceding the date of the application for the grant.\n**(3) Permitted**\nFunds appropriated by Congress for the activities of any agency of a Tribal government or the Bureau of Indian Affairs may be used to provide the non-Federal share of the cost of programs or projects funded under this section.\n##### (e) Waivers\n**(1) In general**\nIn a case of demonstrated economic hardship of an applicant for a grant under this section, the Administrator of FEMA may\u2014\n**(A)**\nwaive the requirements of subsection (d)(1); or\n**(B)**\nwaive or reduce the application of subsection (a)(5) or (d)(2).\n**(2) Guidelines**\n**(A) In general**\nThe Administrator of FEMA shall establish and publish guidelines for determining what constitutes economic hardship for purposes of paragraph (1).\n**(B) Consultation**\nIn developing guidelines under subparagraph (A), the Administrator of FEMA shall consult with individuals who are\u2014\n**(i)**\nrecognized for expertise in emergency medical services provided by fire services, community paramedicine, fall prevention, or the economic affairs of State or local governments; and\n**(ii)**\nmembers of national fire service organizations or national organizations representing the interests of State or local governments.\n**(C) Considerations**\nIn developing guidelines under subparagraph (A), the Administrator of FEMA shall consider, with respect to relevant communities, the following:\n**(i)**\nChanges in rates of unemployment from previous years.\n**(ii)**\nWhether the rates of unemployment of the relevant communities are currently and have consistently exceeded the annual national average rates of unemployment.\n**(iii)**\nChanges in percentages of individuals eligible to receive food stamps from previous years.\n**(iv)**\nSuch other factors as the Administrator of FEMA considers appropriate.\n##### (f) Performance evaluation\n**(1) In general**\nThe Administrator of FEMA shall establish a performance assessment system, including quantifiable performance metrics, to evaluate the extent to which grants awarded under this section are furthering the purposes of this section.\n**(2) Submittal of information**\nThe Administrator of FEMA may require a grant recipient to submit to the Administrator of FEMA any information the Administrator of FEMA considers reasonably necessary to evaluate the implementation of programs to improve home safety and prevent falls for older adults.\n##### (g) Report\nNot later than two years after the date of the enactment of this Act, the Administrator of FEMA shall submit to Congress a report on the experience with, and effectiveness of, grants awarded under this section in meeting the objectives of this section. Such report may include any recommendations the Administrator of FEMA may have for amendments to this section and related provisions of law.\n##### (h) Revocation or suspension of funding\nIf the Administrator of FEMA determines that a grant recipient under this section is not in substantial compliance with the terms and requirements of an approved grant application submitted under this section, the Administrator of FEMA may revoke or suspend funding of such grant, in whole or in part.\n##### (i) Access to documents\n**(1) In general**\nThe Administrator of FEMA shall have access for the purpose of audit and examination to any pertinent books, documents, papers, or records of a grant recipient under this section and to the pertinent books, documents, papers, or records of State and local governments, persons, businesses, and other entities that are involved in programs, projects, or activities for which assistance is provided under this section.\n**(2) Application**\nParagraph (1) shall apply with respect to audits and examinations conducted by the Comptroller General of the United States or by an authorized representative of the Comptroller General.\n##### (j) Definitions\nIn this section:\n**(1) Administrator of FEMA; career fire department; combination fire department; volunteer fire department**\nThe terms Administrator of FEMA , career fire department , combination fire department , and volunteer fire department have the meanings given such terms in section 33(a) of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2229(a) ).\n**(2) Community paramedicine**\nThe term community paramedicine means the operation of first responders, including firefighters, emergency medical technicians (EMTs), and paramedics, in roles that serve to proactively make communities, homes, and residents safer and prevent future medical emergencies.\n**(3) Fall prevention**\nThe term fall prevention means the use of evidence-based measures that decrease fall risks in older adults.\n**(4) Fire service; local**\nThe terms fire service and local have the meanings given such terms in section 4 of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2203 ).\n**(5) Firefighter**\nThe term firefighter has the meaning given the term employee in fire protection activities in section 3(y) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(y) ).\n**(6) State**\nThe term State has the meaning given such term in section 2 of the Homeland Security Act of 2002 ( 6 U.S.C. 101 ).\n##### (k) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated for the purposes of carrying out this section, the following:\n**(A)**\n$1,000,000 for each of fiscal years 2026, 2027, and 2028.\n**(B)**\n$2,000,000 for each of fiscal years 2029, 2030, and 2031.\n**(C)**\n$4,000,000 for each of fiscal years 2032, 2033, and 2034.\n**(D)**\n$7,000,000 for fiscal year 2035.\n**(2) Administrative expenses**\nOf the amounts authorized to be appropriated pursuant to paragraph (1) for a fiscal year, the Administrator of FEMA may use not more than five percent of such amounts to cover salaries and expenses and other administrative costs incurred by the Administrator of FEMA to make grants and provide assistance under this section.\n##### (l) Sunset of authorities\nThis section expires on September 30, 2036.",
      "versionDate": "2025-09-26",
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
        "updateDate": "2025-11-18T17:49:14Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5575ih.xml"
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
      "title": "FASTER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FASTER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Firefighters Assisting Seniors To Emergency Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize grants to fire departments to conduct activities with the goals of reducing falls among older adults and reducing response time when responding to in-home emergencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:22Z"
    }
  ]
}
```
