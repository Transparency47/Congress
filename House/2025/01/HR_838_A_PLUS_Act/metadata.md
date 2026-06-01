# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/838?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/838
- Title: A PLUS Act
- Congress: 119
- Bill type: HR
- Bill number: 838
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-05T21:36:23Z
- Update date including text: 2025-12-05T21:36:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/838",
    "number": "838",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "A PLUS Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:36:23Z",
    "updateDateIncludingText": "2025-12-05T21:36:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:07:25Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NC"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "KY"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr838ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 838\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Moolenaar (for himself, Mr. Edwards , Mr. Guthrie , and Mr. Green of Tennessee ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo allow a State to submit a declaration of intent to the Secretary of Education to combine certain funds to improve the academic achievement of students.\n#### 1. Short title\nThis Act may be cited as the Academic Partnerships Lead Us to Success Act or the A PLUS Act .\n#### 2. Purposes\nThe purposes of this Act are as follows:\n**(1)**\nTo give States and local communities added flexibility to determine how to improve academic achievement and implement education reforms.\n**(2)**\nTo reduce the administrative costs and compliance burden of Federal education programs in order to focus Federal resources on improving academic achievement.\n**(3)**\nTo ensure that States and communities are accountable to the public for advancing the academic achievement of all students, especially disadvantaged children.\n#### 3. Definitions\nIn this Act:\n**(1) In general**\nExcept as otherwise provided, the terms used in this Act have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 et seq. ).\n**(2) Accountability**\nThe term accountability means that public schools are answerable to parents and other taxpayers for the use of public funds and shall report student progress to parents and taxpayers regularly.\n**(3) Declaration of intent**\nThe term declaration of intent means a decision by a State, as determined by State Authorizing Officials or by referendum, to assume full management responsibility for the expenditure of Federal funds for certain eligible programs for the purpose of advancing, on a more comprehensive and effective basis, the educational policy of such State.\n**(4) State**\nThe term State has the meaning given such term in section 1122(e) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6332(e) ).\n**(5) State authorizing officials**\nThe term State Authorizing Officials means the State officials who shall authorize the submission of a declaration of intent, and any amendments thereto, on behalf of the State. Such officials shall include not less than two of the following:\n**(A)**\nThe Governor of the State.\n**(B)**\nThe highest elected education official of the State, if any.\n**(C)**\nThe legislature of the State.\n**(6) State designated officer**\nThe term State Designated Officer means the person designated by the State Authorizing Officials to submit to the Secretary, on behalf of the State, a declaration of intent, and any amendments thereto, and to function as the point-of-contact for the State for the Secretary and others relating to any responsibilities arising under this Act.\n#### 4. Declaration of intent\n##### (a) In general\nEach State is authorized to submit to the Secretary a declaration of intent permitting the State to receive Federal funds on a consolidated basis to manage the expenditure of such funds to advance the educational policy of the State.\n##### (b) Programs eligible for consolidation and permissible use of funds\n**(1) Scope**\nA State may choose to include within the scope of the State's declaration of intent any program for which Congress makes funds available to the State if the program is for a purpose described in the Elementary and Secondary Act of 1965 ( 20 U.S.C. 6301 ). A State may not include any program funded pursuant to the Individuals with Disabilities Education Act ( 20 U.S.C. 1400 et seq. ).\n**(2) Uses of funds**\nFunds made available to a State pursuant to a declaration of intent under this Act shall be used for any educational purpose permitted by State law of the State submitting a declaration of intent.\n**(3) Removal of fiscal and accounting barriers**\nEach State educational agency that operates under a declaration of intent under this Act shall modify or eliminate State fiscal and accounting barriers that prevent local educational agencies and schools from easily consolidating funds from other Federal, State, and local sources in order to improve educational opportunities and reduce unnecessary fiscal and accounting requirements.\n##### (c) Contents of declaration\nEach declaration of intent shall contain\u2014\n**(1)**\na list of eligible programs that are subject to the declaration of intent;\n**(2)**\nan assurance that the submission of the declaration of intent has been authorized by the State Authorizing Officials, specifying the identity of the State Designated Officer;\n**(3)**\nthe duration of the declaration of intent;\n**(4)**\nan assurance that the State will use fiscal control and fund accounting procedures;\n**(5)**\nan assurance that the State will meet the requirements of applicable Federal civil rights laws in carrying out the declaration of intent and in consolidating and using the funds under the declaration of intent;\n**(6)**\nan assurance that in implementing the declaration of intent the State will seek to advance educational opportunities for the disadvantaged;\n**(7)**\na description of the plan for maintaining direct accountability to parents and other citizens of the State; and\n**(8)**\nan assurance that in implementing the declaration of intent, the State will seek to use Federal funds to supplement, rather than supplant, State education funding.\n##### (d) Duration\nThe duration of the declaration of intent shall not exceed 5 years.\n##### (e) Review and recognition by the secretary\n**(1) In general**\nThe Secretary shall review the declaration of intent received from the State Designated Officer not more than 60 days after the date of receipt of such declaration, and shall recognize such declaration of intent unless the declaration of intent fails to meet the requirements under subsection (c).\n**(2) Recognition by operation of law**\nIf the Secretary fails to take action within the time specified in paragraph (1), the declaration of intent, as submitted, shall be deemed to be approved.\n##### (f) Amendment to declaration of intent\n**(1) In general**\nThe State Authorizing Officials may direct the State Designated Officer to submit amendments to a declaration of intent that is in effect. Such amendments shall be submitted to the Secretary and considered by the Secretary in accordance with subsection (e).\n**(2) Amendments authorized**\nA declaration of intent that is in effect may be amended to\u2014\n**(A)**\nexpand the scope of such declaration of intent to encompass additional eligible programs;\n**(B)**\nreduce the scope of such declaration of intent by excluding coverage of a Federal program included in the original declaration of intent;\n**(C)**\nmodify the duration of such declaration of intent; or\n**(D)**\nachieve such other modifications as the State Authorizing Officials deem appropriate.\n**(3) Effective date**\nThe amendment shall specify an effective date. Such effective date shall provide adequate time to assure full compliance with Federal program requirements relating to an eligible program that has been removed from the coverage of the declaration of intent by the proposed amendment.\n**(4) Treatment of program funds withdrawn from declaration of intent**\nBeginning on the effective date of an amendment executed under paragraph (2)(B), each program requirement of each program removed from the declaration of intent shall apply to the State's use of funds made available under the program.\n#### 5. Transparency for results of public education\n##### (a) In general\nEach State operating under a declaration of intent under this Act shall inform parents and the general public regarding the student achievement assessment system, demonstrating student progress relative to the State's determination of student proficiency for the purpose of public accountability to parents and taxpayers.\n##### (b) Accountability system\nThe State shall determine and establish an accountability system to ensure accountability under this Act.\n##### (c) Report on student progress\nNot later than 1 year after the effective date of the declaration of intent, and annually thereafter, a State shall disseminate widely to parents and the general public a report that describes student progress. The report shall include\u2014\n**(1)**\nstudent performance data disaggregated in the same manner as data are disaggregated under section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) ); and\n**(2)**\na description of how the State has used Federal funds to improve academic achievement, reduce achievement disparities between various student groups, and improve educational opportunities for the disadvantaged.\n#### 6. Administrative expenses\n##### (a) In general\nExcept as provided in subsection (b), the amount that a State with a declaration of intent may expend for administrative expenses shall be limited to 1 percent of the aggregate amount of Federal funds made available to the State through the eligible programs included within the scope of such declaration of intent.\n##### (b) States not consolidating funds under part A of title I\nIf the declaration of intent does not include within its scope part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ), the amount spent by the State on administrative expenses shall be limited to 3 percent of the aggregate amount of Federal funds made available to the State pursuant to such declaration of intent.\n#### 7. Equitable participation of private schools\nEach State consolidating and using funds pursuant to a declaration of intent under this Act shall provide for the participation of private school children and teachers in the activities assisted under the declaration of intent in the same manner as participation is provided to private school children and teachers under section 8501 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7881 ).",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-29",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "309",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A PLUS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Academic performance and assessments",
            "updateDate": "2025-03-24T15:21:08Z"
          },
          {
            "name": "Education of the disadvantaged",
            "updateDate": "2025-03-24T15:21:08Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-03-24T15:21:08Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-03-24T15:21:08Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-24T15:21:08Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-24T15:21:08Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-03-24T15:21:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-03T14:16:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
    "originChamber": "House",
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
          "measure-id": "id119hr838",
          "measure-number": "838",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr838v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Academic Partnerships Lead Us to Success Act or the A PLUS Act</strong>\u00a0</p><p>This bill creates a framework under which states may receive federal elementary and secondary education funds on a consolidated basis and use such funds for any educational purpose permitted by state law.</p>"
        },
        "title": "A PLUS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr838.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Academic Partnerships Lead Us to Success Act or the A PLUS Act</strong>\u00a0</p><p>This bill creates a framework under which states may receive federal elementary and secondary education funds on a consolidated basis and use such funds for any educational purpose permitted by state law.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr838"
    },
    "title": "A PLUS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Academic Partnerships Lead Us to Success Act or the A PLUS Act</strong>\u00a0</p><p>This bill creates a framework under which states may receive federal elementary and secondary education funds on a consolidated basis and use such funds for any educational purpose permitted by state law.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr838"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr838ih.xml"
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
      "title": "A PLUS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "A PLUS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Academic Partnerships Lead Us to Success Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow a State to submit a declaration of intent to the Secretary of Education to combine certain funds to improve the academic achievement of students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T05:18:30Z"
    }
  ]
}
```
