# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/527
- Title: Strengthening Wildfire Resiliency Through Satellites Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 527
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-02-04T05:06:20Z
- Update date including text: 2026-02-04T05:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/527",
    "number": "527",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Strengthening Wildfire Resiliency Through Satellites Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:20Z",
    "updateDateIncludingText": "2026-02-04T05:06:20Z"
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
          "date": "2025-01-16T14:05:05Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr527ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 527\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Pettersen (for herself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior, acting through the Director of the United States Geological Survey, to establish a grant program for monitoring wildfires by satellite.\n#### 1. Short title\nThis Act may be cited as the Strengthening Wildfire Resiliency Through Satellites Act of 2025 .\n#### 2. Monitoring wildfires by satellite\n##### (a) Grant program To monitor wildfires by satellite\n**(1) Establishment**\nNot later than one year after the date of the enactment of this section, the Secretary shall establish a competitive grant program under which the Secretary shall make at least three grants to eligible entities to monitor wildfires by satellite (in this section referred to as the Program ).\n**(2) Eligible projects**\nEach eligible entity awarded a grant under the Program shall only use such grant to\u2014\n**(A)**\npurchase and integrate, through a public-private partnership, high-resolution multi- and hyper-spectral full spectrum imaging capability from visible, near-infrared, shortwave infrared, thermal infrared, and radar data from the latest-generation of wildfire monitoring satellites; and\n**(B)**\nuse the data acquired under subparagraph (A), as well as any analyses relating to such data, to detect, assess, respond to, and manage wildfires, with an emphasis on\u2014\n**(i)**\nmonitoring active fire behavior, burned area, intensity, and severity;\n**(ii)**\nensuring the safety and effectiveness of prescribed fire treatments; and\n**(iii)**\nguiding post-fire risk assessment and disaster recovery.\n**(3) Application**\nTo be eligible for a grant under the Program, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n**(4) Grant amount**\nEach grant awarded under the Program shall be in an amount the Secretary determines appropriate.\n**(5) Report**\nNot later than the last day of the second fiscal year beginning after the date of the enactment of this section, the Secretary shall submit to Congress a report that includes\u2014\n**(A)**\nthe number of applications received for a grant under the Program;\n**(B)**\ndetails of each eligible entity that was awarded a grant under the Program;\n**(C)**\nthe impact of the Program on wildfire prevention;\n**(D)**\nany recommendation that the Secretary determines appropriate to establish the Program as a long-term grant program; and\n**(E)**\nany other information on the effectiveness of the Program that the Secretary determines appropriate.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $20,000,000 for each of fiscal years 2026 through 2028 to carry out the Program.\n##### (c) Definitions\nIn this section\u2014\n**(1)**\nthe term eligible entity means a State forester, emergency manager, or equivalent State official; and\n**(2)**\nthe term Secretary means the Secretary of the Interior, acting through the Director of the United States Geological Survey.",
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
        "name": "Emergency Management",
        "updateDate": "2025-02-26T21:11:40Z"
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
          "measure-id": "id119hr527",
          "measure-number": "527",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr527v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strengthening Wildfire Resiliency Through Satellites Act of 2025</strong></p><p>This bill requires the U.S. Geological Survey to establish a competitive grant program to fund satellite monitoring of wildfires. The entities eligible to receive the grants are state foresters, emergency managers, and equivalent state officials. Grant recipients must use the funds for purchasing and integrating satellite data on wildfire monitoring and for using the data to detect and manage wildfires.\u00a0</p>"
        },
        "title": "Strengthening Wildfire Resiliency Through Satellites Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr527.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Wildfire Resiliency Through Satellites Act of 2025</strong></p><p>This bill requires the U.S. Geological Survey to establish a competitive grant program to fund satellite monitoring of wildfires. The entities eligible to receive the grants are state foresters, emergency managers, and equivalent state officials. Grant recipients must use the funds for purchasing and integrating satellite data on wildfire monitoring and for using the data to detect and manage wildfires.\u00a0</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr527"
    },
    "title": "Strengthening Wildfire Resiliency Through Satellites Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Wildfire Resiliency Through Satellites Act of 2025</strong></p><p>This bill requires the U.S. Geological Survey to establish a competitive grant program to fund satellite monitoring of wildfires. The entities eligible to receive the grants are state foresters, emergency managers, and equivalent state officials. Grant recipients must use the funds for purchasing and integrating satellite data on wildfire monitoring and for using the data to detect and manage wildfires.\u00a0</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr527"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr527ih.xml"
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
      "title": "Strengthening Wildfire Resiliency Through Satellites Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T12:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Wildfire Resiliency Through Satellites Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior, acting through the Director of the United States Geological Survey, to establish a grant program for monitoring wildfires by satellite.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T12:03:31Z"
    }
  ]
}
```
