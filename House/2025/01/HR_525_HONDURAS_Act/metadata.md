# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/525
- Title: HONDURAS Act
- Congress: 119
- Bill type: HR
- Bill number: 525
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-01-17T04:41:13Z
- Update date including text: 2026-01-17T04:41:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/525",
    "number": "525",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "HONDURAS Act",
    "type": "HR",
    "updateDate": "2026-01-17T04:41:13Z",
    "updateDateIncludingText": "2026-01-17T04:41:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr525ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 525\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Ogles (for himself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit funding to the Government of the Republic of Honduras.\n#### 1. Short title\nThis Act may be cited as the Honduras Obstinately Neglects Defense and Risks Alienating Security Act or HONDURAS Act .\n#### 2. Prohibition of funding\nNotwithstanding any other provision of law, beginning after the redeployment of United States military and civilian personnel from Soto Cano Air Base in Honduras as a result of the refusal or unwillingness of the Government of the Republic of Honduras to host such personnel, the President is authorized to suspend all assistance to the Republic of Honduras, to include any assistance extended under the May 20, 1954, bilateral military assistance agreement between the United States and Honduras and any subsequent amendments to that agreement.",
      "versionDate": "2025-01-16",
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
        "name": "International Affairs",
        "updateDate": "2025-02-21T12:49:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr525",
          "measure-number": "525",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr525v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Honduras Obstinately Neglects Defense and Risks Alienating Security Act or HONDURAS Act</strong></p><p>This bill authorizes the President to suspend all assistance to Honduras if U.S. military and civilian personnel redeploy from Soto Cano Air Base as the result of the Honduran government's refusal to host such personnel at the base.</p>"
        },
        "title": "HONDURAS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr525.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honduras Obstinately Neglects Defense and Risks Alienating Security Act or HONDURAS Act</strong></p><p>This bill authorizes the President to suspend all assistance to Honduras if U.S. military and civilian personnel redeploy from Soto Cano Air Base as the result of the Honduran government's refusal to host such personnel at the base.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr525"
    },
    "title": "HONDURAS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honduras Obstinately Neglects Defense and Risks Alienating Security Act or HONDURAS Act</strong></p><p>This bill authorizes the President to suspend all assistance to Honduras if U.S. military and civilian personnel redeploy from Soto Cano Air Base as the result of the Honduran government's refusal to host such personnel at the base.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr525"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr525ih.xml"
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
      "title": "HONDURAS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T12:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HONDURAS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honduras Obstinately Neglects Defense and Risks Alienating Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit funding to the Government of the Republic of Honduras.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T12:03:29Z"
    }
  ]
}
```
