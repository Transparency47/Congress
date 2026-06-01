# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5794?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5794
- Title: FEMA Operations Continuity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5794
- Origin chamber: House
- Introduced date: 2025-10-21
- Update date: 2025-12-02T09:05:57Z
- Update date including text: 2025-12-02T09:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-21: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-10-21: Introduced in House

## Actions

- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Introduced in House
- 2025-10-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5794",
    "number": "5794",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "FEMA Operations Continuity Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:57Z",
    "updateDateIncludingText": "2025-12-02T09:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T18:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:52:36Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5794ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5794\nIN THE HOUSE OF REPRESENTATIVES\nOctober 21, 2025 Mr. Bell (for himself, Mr. Moulton , and Mr. Fields ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo authorize the Administrator of the Federal Emergency Management Agency to continue disaster relief, recovery, and mitigation operations funded through the Disaster Relief Fund in the event of a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FEMA Operations Continuity Act of 2025 .\n#### 2. Continuation of FEMA operations during a lapse in appropriations\nNotwithstanding any other provision of law, in the event of a lapse in appropriations, the Administrator of the Federal Emergency Management Agency shall be authorized to\u2014\n**(1)**\ncontinue all disaster relief, recovery, and mitigation operations funded through the Disaster Relief Fund;\n**(2)**\nobligate and disburse Disaster Relief Fund balances for all existing and future disaster declarations, including individual and public assistance under sections 403, 406, 407, 408, and 502 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170b , 5172, 5173, 5174, and 5192); and\n**(3)**\nmaintain personnel and contract support necessary to ensure uninterrupted processing of claims and payments.\n#### 3. Use of Disaster Relief Fund\n##### (a) Availability\nAll unobligated balances in the Disaster Relief Fund shall remain available to the Administrator for expenditure during a lapse in appropriations.\n##### (b) Prohibition on diversion\nNo funds from the Disaster Relief Fund may be withheld, sequestered, or reprogrammed during a lapse in appropriations, except as necessary to comply with section 1341 of title 31, United States Code (commonly referred to as the \u2018Anti-Deficiency Act\u2019).\n#### 4. Exception from government shutdown restrictions\nFor purposes of section 1341 of title 31, United States Code (commonly referred to as the \u2018Anti-Deficiency Act\u2019), operations of the Federal Emergency Management Agency authorized under this Act shall be considered essential to protect human life and property, and therefore exempt from shutdown restrictions.",
      "versionDate": "2025-10-21",
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
        "name": "Emergency Management",
        "updateDate": "2025-10-24T12:40:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-21",
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
          "measure-id": "id119hr5794",
          "measure-number": "5794",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-21",
          "originChamber": "HOUSE",
          "update-date": "2025-10-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5794v00",
            "update-date": "2025-10-27"
          },
          "action-date": "2025-10-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>FEMA Operations Continuity Act of 2025</strong></p><p>This bill authorizes the Federal Emergency Management Agency (FEMA) to continue certain disaster relief, recovery, and mitigation operations during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, the bill authorizes FEMA to</p><ul><li>continue all disaster relief, recovery, and mitigation operations funded through the Disaster Relief Fund (DRF);</li><li>obligate and disburse DRF balances for all existing and future disaster declarations, including individual and public assistance under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act;\u00a0and</li><li>maintain personnel and contract support necessary to ensure uninterrupted processing of claims and payments.</li></ul><p>The bill also (1) requires all unobligated balances in the DRF to remain available to FEMA for expenditure during a lapse in appropriations; and (2) prohibits the funds from being withheld, sequestered, or reprogrammed during a lapse in appropriations, except as necessary to comply with the Antideficiency Act.</p><p>Finally, the bill specifies that, for the purposes of the Antideficiency Act, the FEMA operations authorized by this bill must be considered essential to protect human life and property and are exempt from government shutdown restrictions.</p>"
        },
        "title": "FEMA Operations Continuity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5794.xml",
    "summary": {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Operations Continuity Act of 2025</strong></p><p>This bill authorizes the Federal Emergency Management Agency (FEMA) to continue certain disaster relief, recovery, and mitigation operations during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, the bill authorizes FEMA to</p><ul><li>continue all disaster relief, recovery, and mitigation operations funded through the Disaster Relief Fund (DRF);</li><li>obligate and disburse DRF balances for all existing and future disaster declarations, including individual and public assistance under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act;\u00a0and</li><li>maintain personnel and contract support necessary to ensure uninterrupted processing of claims and payments.</li></ul><p>The bill also (1) requires all unobligated balances in the DRF to remain available to FEMA for expenditure during a lapse in appropriations; and (2) prohibits the funds from being withheld, sequestered, or reprogrammed during a lapse in appropriations, except as necessary to comply with the Antideficiency Act.</p><p>Finally, the bill specifies that, for the purposes of the Antideficiency Act, the FEMA operations authorized by this bill must be considered essential to protect human life and property and are exempt from government shutdown restrictions.</p>",
      "updateDate": "2025-10-27",
      "versionCode": "id119hr5794"
    },
    "title": "FEMA Operations Continuity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Operations Continuity Act of 2025</strong></p><p>This bill authorizes the Federal Emergency Management Agency (FEMA) to continue certain disaster relief, recovery, and mitigation operations during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, the bill authorizes FEMA to</p><ul><li>continue all disaster relief, recovery, and mitigation operations funded through the Disaster Relief Fund (DRF);</li><li>obligate and disburse DRF balances for all existing and future disaster declarations, including individual and public assistance under the Robert\u00a0T. Stafford Disaster Relief and Emergency Assistance Act;\u00a0and</li><li>maintain personnel and contract support necessary to ensure uninterrupted processing of claims and payments.</li></ul><p>The bill also (1) requires all unobligated balances in the DRF to remain available to FEMA for expenditure during a lapse in appropriations; and (2) prohibits the funds from being withheld, sequestered, or reprogrammed during a lapse in appropriations, except as necessary to comply with the Antideficiency Act.</p><p>Finally, the bill specifies that, for the purposes of the Antideficiency Act, the FEMA operations authorized by this bill must be considered essential to protect human life and property and are exempt from government shutdown restrictions.</p>",
      "updateDate": "2025-10-27",
      "versionCode": "id119hr5794"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5794ih.xml"
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
      "title": "FEMA Operations Continuity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T10:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEMA Operations Continuity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Administrator of the Federal Emergency Management Agency to continue disaster relief, recovery, and mitigation operations funded through the Disaster Relief Fund in the event of a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T10:48:12Z"
    }
  ]
}
```
