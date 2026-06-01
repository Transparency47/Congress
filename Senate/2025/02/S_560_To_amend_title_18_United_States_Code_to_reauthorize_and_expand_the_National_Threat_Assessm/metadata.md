# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/560?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/560
- Title: EAGLES Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 560
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-12-05T21:49:52Z
- Update date including text: 2025-12-05T21:49:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/560",
    "number": "560",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "EAGLES Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:49:52Z",
    "updateDateIncludingText": "2025-12-05T21:49:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-13T16:04:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-13",
      "state": "ME"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ME"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s560is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 560\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Grassley (for himself, Ms. Cortez Masto , Mr. Scott of Florida , Mr. King , Ms. Collins , Ms. Hassan , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to reauthorize and expand the National Threat Assessment Center of the Department of Homeland Security.\n#### 1. Short title\nThis Act may be cited as the EAGLES Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOn February 14, 2018, 17 individuals were murdered in a senseless and violent attack on Marjory Stoneman Douglas High School in Parkland Florida, a school whose mascot is the eagle.\n**(2)**\nThese individuals\u2014Alaina Petty, Alex Schachter, Alyssa Alhadeff, Cara Loughran, Carmen Schentrup, Gina Montalto, Helena Ramsay, Jaime Guttenberg, Joaquin Oliver, Luke Hoyer, Martin Duque, Meadow Pollack, Nicholas Dworet, Peter Wang, Aaron Feis, Chris Hixon, and Scott Beigel\u2014lived lives of warmth, joy, determination, service, and love, and their loss is mourned by the Nation.\n**(3)**\nLike many attackers, the shooter in that attack exhibited patterns of threatening and concerning behavior prior to the massacre that were alarming and that should have alerted law enforcement and other Federal, State, and local officials about the potential for violence.\n**(4)**\nActs of targeted violence, including the attack on Marjory Stoneman Douglas High School, are preventable.\n**(5)**\nLives were saved because of the brave and exemplary conduct of many students, teachers, and staff at Marjory Stoneman Douglas High School, including several of the victims of the attack.\n**(6)**\nThe National Threat Assessment Center of the United States Secret Service (referred to in this Act as the Center ) was established in 1998 to conduct research on all forms of targeted violence, including attacks targeting government officials, government facilities, workplaces, houses of worship, K\u201312 schools, universities, and mass attacks in public spaces.\n**(7)**\nResearch published by the Center on targeted violence has shown that\u2014\n**(A)**\nmost incidents were planned in advance;\n**(B)**\nthe attackers\u2019 behavior gave some indication that the individual was planning, or at least contemplating, an attack;\n**(C)**\nmost attackers had already exhibited a pattern of behavior that elicited concern by other people in their lives; and\n**(D)**\nprior to the attack, someone associated with the attacker, such as a family member or peer, often knew the attack was to likely to occur.\n**(8)**\nThrough their research, the Center developed the behavioral threat assessment model of the United States Secret Service for preventing targeted violence, which includes a 3-step process\u2014\n**(A)**\nidentifying individuals who are exhibiting threatening or concerning behaviors that indicate they may pose a risk of violence;\n**(B)**\nassessing whether the individual poses a risk, based on articulable facts; and\n**(C)**\nrisk posed by the individualized proactive and preventive measures.\n**(9)**\nThe behavioral threat assessment model works of the United States Secret Service most effectively when all the relevant parties, including local law enforcement, mental health professionals, workplace managers, school personnel, and members of the community, are part of a comprehensive protocol to identify, assess, and manage a potential threat.\n**(10)**\nThe primary goal of behavioral threat assessment programs is to prevent targeted violence, with an emphasis on providing early intervention and connecting individuals exhibiting threatening or concerning behavior to existing community resources for support.\n**(11)**\nEarly intervention is a proven and effective way to prevent violent conduct that would otherwise harm others and necessitate more punitive action, including criminal penalties.\n**(12)**\nThe parties involved need the appropriate research, guidance, training, and tools to establish the appropriate mechanisms for implementing this type of preventative approach.\n**(13)**\nIn K\u201312 schools, a behavioral threat assessment is a proactive approach to identify, assess, and provide age-appropriate interventions, resources, and supports for students who display behavior that elicits concerns for the safety of themselves or others.\n**(14)**\nThere has been a 79 percent decline in juvenile arrests in K\u201312 school communities that have received training from the Center, thus successfully diverting youth away from the criminal justice system.\n**(15)**\nThe demand from local communities throughout the United States for behavioral threat assessment trainings has significantly increased. Since its inception, the Center has provided over 2,575 training sessions to over 273,000 attendees.\n**(16)**\nFrom fiscal year 2018 to fiscal year 2022, the Center has experienced a 117 percent increase in demand for training sessions, with 5 times as many participants.\n**(17)**\nThe Center additionally provides consultation and follow-up engagements with government agencies, law enforcement, schools, and other organizations with public safety responsibilities. From fiscal year 2018 to fiscal year 2022 the Center has seen a 553 percent increase in consultation activities.\n##### (b) Sense of Congress\nIt is the sense of Congress that a fact-based behavioral threat assessment approach, involving local law enforcement, mental health professionals, workplace managers, school personnel, other public safety officials, and members of the community, is one of the most effective ways to prevent targeted violence impacting communities across the country, and is a fitting memorial to those whose lives were taken in the February 14, 2018, attack on Marjory Stoneman Douglas High School and those who heroically acted to preserve the lives of their friends, students, and colleagues.\n#### 3. Reauthorization and expansion of the national threat assessment center of the Department of Homeland Security\n##### (a) In general\nChapter 203 of title 18, United States Code, is amended by inserting after section 3056A the following:\n3056B. Functions of the National Threat Assessment Center of the United States Secret Service (a) In general There is established a National Threat Assessment Center (in this section referred to as the Center ), to be operated by the United States Secret Service, at the direction of the Secretary of Homeland Security. (b) Functions The functions of the Center shall include the following: (1) Training and education in the area of best practices on threat assessment and the prevention of targeted violence. (2) Consultation on complex threat assessment cases and programs. (3) Research on threat assessment and the prevention of targeted violence, consistent with evidence-based standards and existing laws and regulations. (4) Facilitation of information sharing on threat assessment and the prevention of targeted violence among agencies and organizations with protective or public safety responsibilities, as well as other public or private entities. (5) Development of evidence-based programs to promote the standardization of Federal, State, and local threat assessments and best practices for the prevention of targeted violence. (c) Safe school initiative In carrying out the functions described in subsection (b), the Center shall establish a national program on targeted school violence prevention, focusing on the following activities: (1) Research The Center shall\u2014 (A) conduct research into targeted school violence and evidence-based practices in targeted school violence prevention, including school threat assessment; and (B) publish the findings of the Center on the public website of the United States Secret Service and on the School Safety Clearinghouse website, known as www.SchoolSafety.gov. (2) Training (A) In general The Center shall develop and offer training courses on targeted school violence prevention to agencies with protective or public safety responsibilities and other public or private entities, including local educational agencies. (B) Plan Not later than 1 year after the date of enactment of this section, the Center shall establish a plan to offer its training and other educational resources to public or private entities within each State. (3) Coordination with other Federal agencies The Center shall develop research and training programs under this section in coordination with the Department of Justice, the Department of Education, and the Department of Health and Human Services. (4) Consultation with entities outside the Federal Government The Center is authorized to consult with State and local educational, law enforcement, and mental health officials and private entities in the development of research and training programs under this section. (5) Interactive website The Center may create an interactive website to disseminate information and data on evidence-based practices in targeted school violence prevention. (d) Hiring of additional personnel The Director of the United States Secret Service may hire additional personnel to comply with the requirements of this section, which, if the Director exercises such authority, shall include\u2014 (1) at least 1 employee with expertise in child psychological development; and (2) at least 1 employee with expertise in school threat assessment. (e) Report to Congress Not later than two years after the date of enactment of this section, the Director of the United States Secret Service shall submit to the Committee on the Judiciary, the Committee on Health, Education, Labor, and Pensions, and the Committee on Appropriations of the Senate and the Committee on the Judiciary, the Committee on Education and Workforce, and the Committee on Appropriations of the House of Representatives a report on actions taken by the United States Secret Service to implement provisions of this section, which shall include information relating to the following: (1) The number of employees hired (on a full-time equivalent basis). (2) The number of individuals in each State trained in threat assessment. (3) The number of school districts in each State trained in school threat assessment or targeted school violence prevention. (4) Information on Federal, State, and local agencies trained or otherwise assisted by the Center. (5) A formal evaluation indicating whether the training and other assistance provided by the Center is effective. (6) A formal evaluation indicating whether the training and other assistance provided by the Center was implemented by the school. (7) A summary of the Center\u2019s research activities and findings. (8) A strategic plan for disseminating the Center\u2019s educational and training resources to each State. (f) Authorization of appropriations There is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2030. (g) No funds To provide firearms training Amounts made available to carry out this section may not be used to train any person in the use of a firearm. (h) No effect on other laws Nothing in this section may be construed to preclude or contradict any other provision of law authorizing training in the use of firearms. (i) Termination This section shall terminate on September 30, 2030. (j) Definitions In this section: (1) Evidence-based The term evidence-based means\u2014 (A) strong evidence from at least one well-designed and well-implemented experimental study; (B) moderate evidence from at least one well-designed and well-implemented quasi-experimental study; or (C) promising evidence from at least one well-designed and well-implemented correlational study with statistical controls for selection bias. (2) Local educational agency The term local educational agency has the meaning given such term under section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ). (3) State The term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands. .\n##### (b) Technical, conforming, and clerical amendments\n**(1) Technical and conforming amendment**\nSection 4 of the Presidential Threat Protection Act of 2000 ( 18 U.S.C. 3056 note) is repealed.\n**(2) Clerical amendment**\nThe table of sections for chapter 203 of title 18, United States Code, is amended by inserting after the item relating to section 3056A the following new item:\n3056B. Functions of the National Threat Assessment Center of the United States Secret Service. .",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-13",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1299",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "EAGLES Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "Protection of officials",
            "updateDate": "2025-06-13T19:09:11Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-06-13T19:09:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-13T15:20:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s560",
          "measure-number": "560",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s560v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>EAGLES Act of 2025</strong></p><p>This bill reauthorizes the National Threat Assessment Center (NTAC) within the U.S. Secret Service.</p><p>It reauthorizes the functions of NTAC through FY2030 and expands them to include additional activities related to the prevention of targeted violence, such as the establishment of a national program on targeted school violence prevention.</p>"
        },
        "title": "EAGLES Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s560.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>EAGLES Act of 2025</strong></p><p>This bill reauthorizes the National Threat Assessment Center (NTAC) within the U.S. Secret Service.</p><p>It reauthorizes the functions of NTAC through FY2030 and expands them to include additional activities related to the prevention of targeted violence, such as the establishment of a national program on targeted school violence prevention.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s560"
    },
    "title": "EAGLES Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>EAGLES Act of 2025</strong></p><p>This bill reauthorizes the National Threat Assessment Center (NTAC) within the U.S. Secret Service.</p><p>It reauthorizes the functions of NTAC through FY2030 and expands them to include additional activities related to the prevention of targeted violence, such as the establishment of a national program on targeted school violence prevention.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s560"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s560is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "EAGLES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EAGLES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to reauthorize and expand the National Threat Assessment Center of the Department of Homeland Security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:36Z"
    }
  ]
}
```
