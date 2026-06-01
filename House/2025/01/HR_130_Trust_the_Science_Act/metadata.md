# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/130
- Title: Trust the Science Act
- Congress: 119
- Bill type: HR
- Bill number: 130
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-06T06:46:47Z
- Update date including text: 2025-12-06T06:46:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/130",
    "number": "130",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "B000825",
        "district": "3",
        "firstName": "Lauren",
        "fullName": "Rep. Boebert, Lauren [R-CO-4]",
        "lastName": "Boebert",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Trust the Science Act",
    "type": "HR",
    "updateDate": "2025-12-06T06:46:47Z",
    "updateDateIncludingText": "2025-12-06T06:46:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:22:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr130ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 130\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Boebert introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to reissue regulations removing the gray wolf from the list of endangered and threatened wildlife under the Endangered Species Act of 1973.\n#### 1. Short title\nThis Act may be cited as the Trust the Science Act .\n#### 2. Removing the gray wolf from the list of endangered and threatened wildlife\nNot later than 60 days after the date of enactment of this section, the Secretary of the Interior shall reissue the final rule entitled Endangered and Threatened Wildlife and Plants; Removing the Gray Wolf (Canis lupus) From the List of Endangered and Threatened Wildlife and published on November 3, 2020 (85 Fed. Reg. 69778).\n#### 3. No judicial review\nReissuance of the final rule under section 2 shall not be subject to judicial review.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-10-03",
        "text": "Placed on the Union Calendar, Calendar No. 285."
      },
      "number": "845",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Pet and Livestock Protection Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-04-16T17:42:46Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-04-16T17:42:46Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-04-16T17:42:46Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-04-16T17:42:46Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-04-16T17:42:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Animals",
        "updateDate": "2025-01-31T18:53:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr130",
          "measure-number": "130",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr130v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Trust the Science Act</b></p> <p>This bill directs the Department of the Interior to remove protections for the gray wolf under the Endangered Species Act of 1973 (ESA). Specifically, the bill requires Interior to reissue the final rule titled <i>Endangered and Threatened Wildlife and Plants; Removing the Gray Wolf (Canis lupus) From the List of Endangered and Threatened Wildlife</i> and published on November 3, 2020.</p> <p>The rule removed the gray wolf in the lower 48 United States, except for the Mexican wolf (<em>C. l. baileyi</em>) subspecies, from the endangered and threatened species list. However, the U.S. District Court for the Northern District of California vacated the rule on February 10, 2022. As a result, the gray wolf reattained the protection status it had prior to the rule's promulgation. </p> <p>The bill also prohibits the reissuance of the rule from being subject to judicial review.</p>"
        },
        "title": "Trust the Science Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr130.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Trust the Science Act</b></p> <p>This bill directs the Department of the Interior to remove protections for the gray wolf under the Endangered Species Act of 1973 (ESA). Specifically, the bill requires Interior to reissue the final rule titled <i>Endangered and Threatened Wildlife and Plants; Removing the Gray Wolf (Canis lupus) From the List of Endangered and Threatened Wildlife</i> and published on November 3, 2020.</p> <p>The rule removed the gray wolf in the lower 48 United States, except for the Mexican wolf (<em>C. l. baileyi</em>) subspecies, from the endangered and threatened species list. However, the U.S. District Court for the Northern District of California vacated the rule on February 10, 2022. As a result, the gray wolf reattained the protection status it had prior to the rule's promulgation. </p> <p>The bill also prohibits the reissuance of the rule from being subject to judicial review.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr130"
    },
    "title": "Trust the Science Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Trust the Science Act</b></p> <p>This bill directs the Department of the Interior to remove protections for the gray wolf under the Endangered Species Act of 1973 (ESA). Specifically, the bill requires Interior to reissue the final rule titled <i>Endangered and Threatened Wildlife and Plants; Removing the Gray Wolf (Canis lupus) From the List of Endangered and Threatened Wildlife</i> and published on November 3, 2020.</p> <p>The rule removed the gray wolf in the lower 48 United States, except for the Mexican wolf (<em>C. l. baileyi</em>) subspecies, from the endangered and threatened species list. However, the U.S. District Court for the Northern District of California vacated the rule on February 10, 2022. As a result, the gray wolf reattained the protection status it had prior to the rule's promulgation. </p> <p>The bill also prohibits the reissuance of the rule from being subject to judicial review.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr130"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr130ih.xml"
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
      "title": "Trust the Science Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Trust the Science Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to reissue regulations removing the gray wolf from the list of endangered and threatened wildlife under the Endangered Species Act of 1973.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:25Z"
    }
  ]
}
```
