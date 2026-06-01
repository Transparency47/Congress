# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4137
- Title: RECOVER Act
- Congress: 119
- Bill type: S
- Bill number: 4137
- Origin chamber: Senate
- Introduced date: 2026-03-18
- Update date: 2026-04-02T17:46:15Z
- Update date including text: 2026-04-02T17:46:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in Senate
- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2026-03-18: Introduced in Senate

## Actions

- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4137",
    "number": "4137",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "RECOVER Act",
    "type": "S",
    "updateDate": "2026-04-02T17:46:15Z",
    "updateDateIncludingText": "2026-04-02T17:46:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T22:29:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4137is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4137\nIN THE SENATE OF THE UNITED STATES\nMarch 18, 2026 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a pilot program to provide grants to outpatient mental health facilities for the provision of culturally competent, evidence-based mental health care for veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Recognizing Community Organizations for Veteran Engagement and Recovery Act or the RECOVER Act .\n#### 2. Department of Veterans Affairs pilot program to provide grants to medical facilities for the provision of culturally competent, evidence-based mental health care for veterans\n##### (a) Establishment\nThe Secretary of Veterans Affairs shall carry out a pilot program under which the Secretary shall award grants to mental health care providers for the provision of culturally competent, evidence-based mental health care for veterans (in this section referred to as the pilot program ).\n##### (b) Duration\nThe Secretary shall carry out the pilot program for a period of three years.\n##### (c) Eligibility\nTo be eligible to receive a grant under the pilot program, a mental health care provider shall\u2014\n**(1)**\nbe a non-profit organization;\n**(2)**\nhave operated at least one outpatient mental health facility in the United States for a continuous period of not less than three years; and\n**(3)**\nsubmit to the Secretary an application that includes such information and assurances as the Secretary may require, including\u2014\n**(A)**\nan identification of the outpatient facility or facilities where the provider will provide mental health care to veterans using funds provided under the grant;\n**(B)**\na plan under which at least one clinician employed by the provider at each facility for which a grant is made is trained to provide culturally competent veterans mental health care pursuant to the requirements established by the Secretary under subsection (g); and\n**(C)**\nan identification of the percentage of the operating budget for each such facility that was provided through Federal grants during the fiscal year preceding the year during which the application is submitted.\n##### (d) Use of funds\n**(1) In general**\nThe recipient of a grant under the pilot program shall use the grant\u2014\n**(A)**\nto provide culturally competent, evidence-based mental health care for veterans;\n**(B)**\nto operate an existing outpatient mental health facility or establish a new outpatient mental health facility for the purpose of providing such care; and\n**(C)**\nto encourage veterans who are eligible for enrollment in the patient enrollment system of the Department of Veterans Affairs under section 1705 of title 38, United States Code, to enroll in such system and to receive medical services furnished by the Department.\n**(2) Limitations**\nThe recipient of a grant under the pilot program may not\u2014\n**(A)**\ncharge any veteran a fee associated with the receipt of mental health care under the pilot program; or\n**(B)**\nrefuse to provide mental health care to any veteran on the basis that the veteran is not eligible for reimbursement for such care under a health plan contract or any Federal, State, or local government program.\n**(3) Reimbursement**\nNothing in this subsection shall prevent the recipient of a grant under the pilot program from seeking or receiving reimbursement for all, or a portion, of the mental health care provided to a veteran, including reimbursement under a health plan contract, the Veterans Community Care Program under section 1703 of title 38, United States Code, or any other Federal, State, or local government program.\n##### (e) Selection of facilities\nIn selecting outpatient mental health facilities for the receipt of grants under the pilot program, the Secretary\u2014\n**(1)**\nshall ensure that grants are distributed evenly among outpatient mental health facilities located in rural and urban areas;\n**(2)**\nmay consider the proportion of veterans historically served by the outpatient mental health facilities; and\n**(3)**\nmay prioritize outpatient mental health facilities located in areas that the Secretary determines\u2014\n**(A)**\nare medically underserved;\n**(B)**\nhave large veteran populations;\n**(C)**\nare located near military installations; or\n**(D)**\nhave large numbers of veterans at high risk of suicide.\n##### (f) Amount of grant\n**(1) In general**\n**(A) In general**\nExcept as provided in subparagraph (B), no grant under the pilot program for a facility for any fiscal year may exceed $1,500,000.\n**(B) Limitation**\nIn the case of an outpatient mental health facility for which not less than 50 percent of the operating budget of the facility for the preceding fiscal year was provided through Federal grants, no grant under the pilot program for the facility for any fiscal year may exceed the lesser of\u2014\n**(i)**\n50 percent of the operating budget of the facility; or\n**(ii)**\n$1,500,000.\n**(2) Multiple grants**\nThe recipient of a grant under the pilot program\u2014\n**(A)**\nmay apply for, and receive, grants for more than one facility of the recipient for any fiscal year; and\n**(B)**\nmay apply for, and receive, a grant for a facility that has already received a grant under the pilot program.\n##### (g) Training requirement\nThe Secretary shall establish the requirements for the training referred to in subsection (c)(3)(B).\n##### (h) Regulations\nThe Secretary shall prescribe regulations to carry out this section, which shall include a requirement that each recipient of a grant under the pilot program shall\u2014\n**(1)**\ndemonstrate the capacity to provide accountability;\n**(2)**\ndemonstrate clinical outcomes; and\n**(3)**\njustify the effective use of any private investment funds or Federal grant funds through data collection and reporting metrics.\n##### (i) Report\nNot later than 180 days after the completion of the pilot program, the Secretary shall submit to Congress a report on the pilot program that includes the following:\n**(1)**\nThe number of veterans who received mental health care under the pilot program.\n**(2)**\nAn identification of the demographics of the veterans served.\n**(3)**\nAn identification of the types of mental health care provided and the time period for which such care was provided.\n**(4)**\nAn identification of outcomes of the pilot program.\n**(5)**\nThe number of veterans who received mental health care under the pilot program and subsequently enrolled in the patient enrollment system of the Department of Veterans Affairs under section 1705 of title 38, United States Code.\n**(6)**\nAn identification of any obstacles faced by grant recipients in providing mental health care under the pilot program.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out the pilot program $20,000,000 for each of fiscal years 2025 through 2027.",
      "versionDate": "2026-03-18",
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
        "actionDate": "2026-01-13",
        "text": "Subcommittee Hearings Held"
      },
      "number": "2283",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Recognizing Community Organizations for Veteran Engagement and Recovery Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-01T20:33:24Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4137is.xml"
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
      "title": "RECOVER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RECOVER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recognizing Community Organizations for Veteran Engagement and Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to carry out a pilot program to provide grants to outpatient mental health facilities for the provision of culturally competent, evidence-based mental health care for veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:37Z"
    }
  ]
}
```
