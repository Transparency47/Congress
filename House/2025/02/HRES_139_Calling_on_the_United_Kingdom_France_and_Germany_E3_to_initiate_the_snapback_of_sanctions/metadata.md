# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/139
- Title: Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).
- Congress: 119
- Bill type: HRES
- Bill number: 139
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-12-05T22:58:22Z
- Update date including text: 2025-12-05T22:58:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-14 - Committee: Submitted in House
- Latest action: 2025-02-14: Submitted in House

## Actions

- 2025-02-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-02-14 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/139",
    "number": "139",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
    "type": "HRES",
    "updateDate": "2025-12-05T22:58:22Z",
    "updateDateIncludingText": "2025-12-05T22:58:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-14T18:32:40Z",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-14",
      "state": "NJ"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "CA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "SC"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "AR"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "WA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres139ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 139\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Ms. Tenney (for herself, Mr. Gottheimer , Mr. Weber of Texas , Mr. LaMalfa , and Mr. Wilson of South Carolina ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nCalling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).\nThat the House of Representatives\u2014\n**(1)**\nrecognizes that Iran\u2019s possession of a nuclear weapon would threaten not only the security of the United States, but global security at large, including United States allies and partners in Europe and the Middle East;\n**(2)**\ncondemns the Government of Iran\u2019s flagrant and repeated violations of commitments it made under the JCPOA and its international obligations under UNSCR 2231;\n**(3)**\ncondemns the Russian Federation and the People\u2019s Republic of China, who remain participants in the JCPOA, for their role in supporting Iran\u2019s malign activities;\n**(4)**\nreaffirms that the United States Government maintains the right to take any necessary measures to prevent the Government of Iran from acquiring nuclear weapons;\n**(5)**\nsupports the imposition and enforcement of robust sanctions on Iran for it nuclear and missile programs and on entities and individuals involved in these programs to deter further proliferation efforts; and\n**(6)**\nurges the E3 to invoke the snapback of United Nations sanctions against Iran under UNSCR 2231 as soon as possible before the option expires on October 18, 2025.",
      "versionDate": "2025-02-14",
      "versionType": "IH"
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
        "text": "Referred to the Committee on Foreign Relations. (text: CR S982)"
      },
      "number": "81",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
      "type": "SRES"
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
        "updateDate": "2025-02-20T13:55:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hres139",
          "measure-number": "139",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres139v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p>The resolution urges the E3 (the United Kingdom, France, and Germany) to invoke the snapback of United Nations (UN) sanctions against Iran under UN Security Council Resolution 2231 before the option expires on October 18, 2025.\u00a0</p><p>This resolution also (1) recognizes that Iran's possession of a nuclear weapon would threaten U.S. and global security, (2) condemns Iran's repeated violations of certain international commitments related to nuclear weapons, and (3) reaffirms that the United States maintains the right to prevent Iran from acquiring nuclear weapons.</p>"
        },
        "title": "Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015)."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres139.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p>The resolution urges the E3 (the United Kingdom, France, and Germany) to invoke the snapback of United Nations (UN) sanctions against Iran under UN Security Council Resolution 2231 before the option expires on October 18, 2025.\u00a0</p><p>This resolution also (1) recognizes that Iran's possession of a nuclear weapon would threaten U.S. and global security, (2) condemns Iran's repeated violations of certain international commitments related to nuclear weapons, and (3) reaffirms that the United States maintains the right to prevent Iran from acquiring nuclear weapons.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hres139"
    },
    "title": "Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015)."
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p>The resolution urges the E3 (the United Kingdom, France, and Germany) to invoke the snapback of United Nations (UN) sanctions against Iran under UN Security Council Resolution 2231 before the option expires on October 18, 2025.\u00a0</p><p>This resolution also (1) recognizes that Iran's possession of a nuclear weapon would threaten U.S. and global security, (2) condemns Iran's repeated violations of certain international commitments related to nuclear weapons, and (3) reaffirms that the United States maintains the right to prevent Iran from acquiring nuclear weapons.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hres139"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres139ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-15T09:18:25Z"
    },
    {
      "title": "Calling on the United Kingdom, France, and Germany (E3) to initiate the snapback of sanctions on Iran under United Nations Security Council Resolution 2231 (2015).",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-15T09:07:20Z"
    }
  ]
}
```
