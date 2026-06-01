# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/906
- Title: Peer to Peer Mental Health Support Act
- Congress: 119
- Bill type: S
- Bill number: 906
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-04-30T11:03:19Z
- Update date including text: 2026-04-30T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/906",
    "number": "906",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Peer to Peer Mental Health Support Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:19Z",
    "updateDateIncludingText": "2026-04-30T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
        "item": [
          {
            "date": "2025-03-06T21:10:38Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-06T21:10:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AK"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s906is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 906\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Hickenlooper (for himself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require the Secretary of Health and Human Services to carry out a pilot program to support evidence-based mental health peer support activities for students.\n#### 1. Short title\nThis Act may be cited as the Peer to Peer Mental Health Support Act .\n#### 2. Peer-to-peer mental health support\n##### (a) In general\nThe Assistant Secretary for Mental Health and Substance Use (referred to in this section as the Assistant Secretary ), in consultation with the Secretary of Education, may, as appropriate and within a relevant existing program, carry out a pilot program and make awards, on a competitive basis, to eligible entities to support evidence-based mental health peer support activities for students enrolled in secondary schools (as such term is defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )).\n##### (b) Eligibility\nTo be eligible to receive an award under this section, an entity shall\u2014\n**(1)**\nbe a State, political subdivision of a State, territory, or Indian Tribe or Tribal organization (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); and\n**(2)**\nsubmit to the Assistant Secretary an application at such time, in such manner, and containing such information as the Assistant Secretary may require, including a description of how the entity will measure and evaluate progress of the program in improving student mental health outcomes.\n##### (c) Use of amounts\n**(1) In general**\nSubject to paragraph (2), an eligible entity may use amounts provided under this section to implement or operate evidence-based mental health peer support activities in 1 or more secondary schools (as such term is defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )) within the jurisdiction of such eligible entity, which may include providing training, as appropriate, to students, adult supervisors, and other appropriate individuals to improve the early identification of, response to, and recovery supports for mental health and substance use challenges, reduce associated risks, and promote resiliency.\n**(2) Program oversight**\nAn eligible entity shall ensure that mental health peer support activities under paragraph (1) are overseen by a school-based mental health professional.\n**(3) FERPA**\nAny education records of the student collected or maintained under this section shall have the protections provided in section 444 of the General Education Provisions Act ( 20 U.S.C. 1232g ).\n##### (d) Evaluation; report\n**(1) Evaluation**\nThe Assistant Secretary shall carry out an evaluation to measure the efficacy of the program under this section. The evaluation shall\u2014\n**(A)**\nmeasure participation rates in mental health peer support activities, including any associated trends;\n**(B)**\ndescribe the specific trainings provided, or other activities carried out under the pilot program;\n**(C)**\nassess whether such mental health peer support activities impacted mental health outcomes of participating students; and\n**(D)**\nmeasure the effectiveness of the pilot program in connecting students to professional mental health services compared to other evidence-based strategies.\n**(2) Report**\nThe Assistant Secretary shall prepare and submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committees on Energy and Commerce and Education and Workforce of the House of Representatives a report containing the results of the evaluation conducted under paragraph (1).\n##### (e) Technical assistance\nThe Assistant Secretary, in coordination with the Secretary of Education, shall provide technical assistance to eligible entities applying for and receiving an award under this section, including the identification and dissemination of best practices for mental health peer support programs for students.\n##### (f) Rule of construction\nSection 4001 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7101 ) shall apply to an entity receiving a grant, contract, or cooperative agreement under this section in the same manner as such section applies to an entity receiving funding under title IV of such Act, except that section 4001(a)(2)(B)(i) of such Act shall not apply.\n##### (g) Sunset\nThis section shall terminate on September 30, 2029.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-09-15",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5353",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Peer to Peer Mental Health Support Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-31T15:16:12Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s906is.xml"
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
      "title": "Peer to Peer Mental Health Support Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Peer to Peer Mental Health Support Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Health and Human Services to carry out a pilot program to support evidence-based mental health peer support activities for students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:30Z"
    }
  ]
}
```
