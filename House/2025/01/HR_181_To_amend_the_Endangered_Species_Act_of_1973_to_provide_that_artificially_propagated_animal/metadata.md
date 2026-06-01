# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/181?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/181
- Title: To amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 181
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-18T15:39:53Z
- Update date including text: 2025-02-18T15:39:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/181",
    "number": "181",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-02-18T15:39:53Z",
    "updateDateIncludingText": "2025-02-18T15:39:53Z"
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
          "date": "2025-01-03T16:24:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr181ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 181\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. McClintock introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes.\n#### 1. Treatment of artificially propagated animals\nSection 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 ) is amended by adding at the end the following new subsection:\n(j) Treatment of artificially propagated animals The Secretary shall not distinguish between naturally propagated animals and artificially propagated animals in making any determination under this Act. .\n#### 2. Artificial propagation for mitigation purposes\n##### (a) In general\nSection 14 of the Endangered Species Act of 1973 (relating to repeals of provisions of law, which have executed) is amended to read as follows:\n14. Artificial propagation for mitigation purposes The Secretary shall authorize the use of artificial propagation of animals of a species for purposes of any mitigation required under this Act with respect to such species. .\n##### (b) Conforming amendment\nThe table of contents in the first section of such Act is amended by striking the item relating to such section and inserting the following:\nSec. 14. Artificial propagation for mitigation purposes. .\n#### 3. Application\nThe amendments made by this Act shall apply with respect to a species without regard to whether the species was determined to be an endangered species or threatened species under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ) before, on, or after the date of enactment of this Act.",
      "versionDate": "2025-01-03",
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
        "name": "Environmental Protection",
        "updateDate": "2025-02-04T12:31:44Z"
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
          "measure-id": "id119hr181",
          "measure-number": "181",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr181v00",
            "update-date": "2025-02-18"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires naturally propagated animals (i.e., wild animals) and artificially propagated animals to be treated the same under the Endangered Species Act of 1973 (ESA). </p> <p>Specifically, distinctions between naturally propagated animals and artificially propagated animals may not be made when the federal government makes determinations under the ESA, such as determinations to designate endangered species, threatened species, or critical habitats. </p> <p>In addition, the bill requires the U.S. Fish and Wildlife Service and the National Marine Fisheries Service to authorize the use of artificial propagation of animals of a species when mitigation is required under the ESA.</p> <p>This bill applies to all endangered or threatened species regardless of when they were listed as endangered or threatened.</p>"
        },
        "title": "To amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr181.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires naturally propagated animals (i.e., wild animals) and artificially propagated animals to be treated the same under the Endangered Species Act of 1973 (ESA). </p> <p>Specifically, distinctions between naturally propagated animals and artificially propagated animals may not be made when the federal government makes determinations under the ESA, such as determinations to designate endangered species, threatened species, or critical habitats. </p> <p>In addition, the bill requires the U.S. Fish and Wildlife Service and the National Marine Fisheries Service to authorize the use of artificial propagation of animals of a species when mitigation is required under the ESA.</p> <p>This bill applies to all endangered or threatened species regardless of when they were listed as endangered or threatened.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr181"
    },
    "title": "To amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires naturally propagated animals (i.e., wild animals) and artificially propagated animals to be treated the same under the Endangered Species Act of 1973 (ESA). </p> <p>Specifically, distinctions between naturally propagated animals and artificially propagated animals may not be made when the federal government makes determinations under the ESA, such as determinations to designate endangered species, threatened species, or critical habitats. </p> <p>In addition, the bill requires the U.S. Fish and Wildlife Service and the National Marine Fisheries Service to authorize the use of artificial propagation of animals of a species when mitigation is required under the ESA.</p> <p>This bill applies to all endangered or threatened species regardless of when they were listed as endangered or threatened.</p>",
      "updateDate": "2025-02-18",
      "versionCode": "id119hr181"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr181ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T09:18:29Z"
    },
    {
      "title": "To amend the Endangered Species Act of 1973 to provide that artificially propagated animals shall be treated the same under that Act as naturally propagated animals, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:30Z"
    }
  ]
}
```
