# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7112
- Title: Veterans’ Bill of Rights Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7112
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-05-22T08:08:45Z
- Update date including text: 2026-05-22T08:08:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7112",
    "number": "7112",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Veterans\u2019 Bill of Rights Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:45Z",
    "updateDateIncludingText": "2026-05-22T08:08:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-15T14:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7112ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7112\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Veterans Affairs to carry out efforts to inform veterans of their rights with regards to the receipt of health care, benefits, and services furnished under provisions of law administered by the Secretary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Bill of Rights Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States has a solemn obligation, articulated by President Abraham Lincoln in 1865, to care for him who shall have borne the battle, and for his widow, and his orphan .\n**(2)**\nVeterans transitioning to civilian life from service in the Armed Forces deserve timely access to health care, benefits, and information, as well as respect, dignity, and transparency in all interactions with the Department of Veterans Affairs.\n**(3)**\nThe responsibilities of the Secretary of Veterans Affairs require that veterans\u2019 rights be clearly codified to ensure accountability and consistent nationwide administration of benefits and services.\n#### 3. Veterans\u2019 Bill of Rights\n##### (a) In general\nThe Secretary of Veterans Affairs shall carry out efforts to inform veterans of their rights with regards to the receipt of health care, benefits, and services furnished under provisions of law administered by the Secretary.\n##### (b) Elements\nIn carrying out subsection (a), the Secretary shall ensure that veterans are aware of their rights with respect to the following:\n**(1) Access to VA or VA-authorized providers**\nVeterans have the right to receive health care from the Department of Veterans Affairs or, when eligible under Federal law, from community providers authorized by the Department.\n**(2) Respect and dignity**\nThe right to be treated with courtesy, respect, and dignity in all interactions with personnel of the Department.\n**(3) Informed consent**\nThe right to receive clear, complete information about treatment options and to provide informed consent for care furnished under laws administered by the Secretary.\n**(4) Awareness of benefits**\nThe right to receive comprehensive, understandable information about benefits, programs, and services for which the veteran may be eligible or entitled under laws administered by the Secretary.\n**(5) Access to benefits**\nThe right to apply for benefits furnished under provisions of law administered by the Secretary at any time and to receive clear explanations from the Department regarding eligibility determinations concerning such benefits.\n**(6) Health care without retaliation**\nThe right to seek care or raise concerns without fear of stigma, retaliation, or adverse action from the Department.\n**(7) Privacy**\nThe right to the protection of personal information and medical records consistent with provisions of Federal law relating to privacy, protection of personal information, and medical records.\n**(8) Right to grievance redress**\nThe right to file complaints concerning services furnished by the Department and to receive timely, thorough investigation and resolution of those complaints.\n**(9) Transparent communication**\nThe right to clear written notification from the Department regarding the status of claims, benefits, and appeals filed with the Department.\n**(10) Appeal and fair hearing**\nThe right to appeal adverse decisions of the Secretary and to receive fair hearings from the Department within a reasonable time.\n##### (c) Responsibilities\nThe Secretary shall\u2014\n**(1)**\nintegrate the rights described in subsection (b) into all Department of Veterans Affairs policies, directives, patient-facing materials, and employee training programs;\n**(2)**\nensure every employee of the Department receives annual training on such rights;\n**(3)**\nprominently display such rights at all Department facilities and the website of the Department;\n**(4)**\nin coordination with the Secretary of Defense and the Secretary of Labor, include a dedicated instruction module on the rights described in subsection (b) as part of the curriculum for the Transition Assistance Program (TAP) under section 1144 of title 10, United States Code;\n**(5)**\nnot later than 180 days after the date of the enactment of this Act, ensure that the rights described in subsection (b) are accessible through a prominent, dedicated feature within the official mobile application of the Department of Veterans Affairs and the eBenefits portal (or any successor personal benefits portal);\n**(6)**\nrequire each Department medical facility to designate a patient advocate or ombudsman to conduct an annual internal audit to assess facility compliance with the rights described in subsection (b), including a review of veteran satisfaction surveys and the timeliness of grievance resolutions; and\n**(7)**\nensure that any written or electronic acknowledgment of a claim for benefits or an application for health care services includes a summary statement of the rights described in subsection (b), emphasizing the veteran\u2019s right to transparent communication and grievance redress.\n##### (d) Rule of construction\nThe provisions of this section shall not be construed\u2014\n**(1)**\nto create a cause of action for damages or judicially enforceable rights beyond those already established under Federal law; or\n**(2)**\nto alter statutory eligibility requirements for care or benefits furnished under laws administered by the Secretary.",
      "versionDate": "2026-01-15",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-04-29",
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "3653",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans\u2019 Bill of Rights Act of 2026",
      "type": "S"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-13T22:31:30Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7112ih.xml"
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
      "title": "Veterans\u2019 Bill of Rights Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Bill of Rights Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to carry out efforts to inform veterans of their rights with regards to the receipt of health care, benefits, and services furnished under provisions of law administered by the Secretary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:42Z"
    }
  ]
}
```
