# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5482?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5482
- Title: Prevent Youth Suicide Act
- Congress: 119
- Bill type: HR
- Bill number: 5482
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-19T09:07:43Z
- Update date including text: 2025-12-19T09:07:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5482",
    "number": "5482",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Prevent Youth Suicide Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:43Z",
    "updateDateIncludingText": "2025-12-19T09:07:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
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
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5482ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5482\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Nunn of Iowa (for himself and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require the Secretary of Education to issue a rule requiring schools to implement protocols for suicide prevention, postvention, and trauma-informed care.\n#### 1. Short title\nThis Act may be cited as the Prevent Youth Suicide Act .\n#### 2. Rules on protocols for suicide prevention at any educational agency or institution serving students in grades 6 through grade 12\n##### (a) Rule\nNot later than 210 days after the date of enactment of this Act, the Secretary of Education shall issue a rule requiring, as a condition of receipt of funds under an applicable program, that an educational agency or institution carry out each of the following:\n**(1) School-based suicide prevention protocols**\nThe development and implementation of evidence-based suicide prevention programs tailored to the needs of students, which shall include\u2014\n**(A)**\nbiennial, evidence-based training for staff and faculty to\u2014\n**(i)**\nidentify signs of distress and risk factors for suicide in students; and\n**(ii)**\nin a case in which a student has been identified as exhibiting such signs or risk factors, guidelines for reporting such identification to parents and guidance counselors, and responding to concerns from such parents and counselors;\n**(B)**\nestablishing a referral system to connect students in need to appropriate mental health resources at school and outside of school; and\n**(C)**\nconducting awareness campaigns and educational initiatives to reduce stigma associated with seeking help for mental health concerns.\n**(2) Suicide postvention support**\nThe development and implementation of a suicide postvention plan to address the aftermath of a suicide, focusing on providing support to affected students, staff, and the broader community, which shall include\u2014\n**(A)**\nguidelines for communication, memorialization, and resources for grief counseling; and\n**(B)**\ncollaboration with mental health professionals and community organizations to ensure comprehensive postvention support.\n**(3) Trauma-informed care**\nThe adoption of a trauma-informed approach in policies and practices to create a safe and supportive environment for all students, which shall include the provision of biennial trauma-sensitive training for school staff to help such staff understand the potential impact of trauma on students and to promote appropriate responses.\n##### (b) Additional requirements for the Secretary of Education\n**(1) Technical assistance**\nThe Secretary shall provide each educational agency or institution subject to the rule issued under subsection (a) with the resources, guidelines, and technical assistance to comply with the requirements of such rule.\n**(2) Compliance monitoring**\nThe Secretary shall establish to ensure compliance with the rule issued under subsection (a), which shall include periodic assessments, evaluations, and audits of each such educational agency or institution.\n**(3) Feedback and improvement**\nThe Secretary shall\u2014\n**(A)**\nencourage educational agencies and institutions to provide feedback to the Secretary on the effectiveness of the requirements issued under the rule; and\n**(B)**\nreview such feedback and make necessary revisions to such rule.\n#### 3. Definitions\nIn this Act:\n**(1) Applicable program**\nThe term applicable program has the meaning given the term in section 400 of the General Education Provisions Act ( 20 U.S.C. 1221 ).\n**(2) Educational agency or institution**\nThe term educational agency or institution means an educational agency or institution (as defined in section 444(a)(3) of the General Education Provisions Act ( 20 U.S.C. 1232g )) that serves students in any grade from grade 6 through grade 12, as determined under State law.\n**(3) Parent**\nThe term parent has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(4) Secretary**\nThe term Secretary means the Secretary of Education.\n**(5) Suicide postvention**\nThe term suicide postvention means activities and support provided after a suicide has occurred, designed to help individuals cope with the loss, minimize potential negative impacts, and prevent contagion.\n**(6) Suicide prevention**\nThe term suicide prevention means comprehensive strategies and actions aimed at identifying individuals at risk of suicide, providing appropriate interventions, and fostering a supportive environment to reduce the likelihood of suicidal behavior.\n**(7) Trauma-informed care**\nThe term trauma-informed care means an approach based on an understanding of the vulnerabilities and triggers of individuals who have experienced trauma, recognize the role trauma has played in the lives of those individuals, recognize the presence of trauma symptoms and their onset, are supportive of trauma recovery, and avoid further traumatization.",
      "versionDate": "2025-09-18",
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
        "name": "Education",
        "updateDate": "2025-11-18T15:46:14Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5482ih.xml"
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
      "title": "Prevent Youth Suicide Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prevent Youth Suicide Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Education to issue a rule requiring schools to implement protocols for suicide prevention, postvention, and trauma-informed care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:12Z"
    }
  ]
}
```
