# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/766?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/766
- Title: SEWER Act
- Congress: 119
- Bill type: HR
- Bill number: 766
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-04-09T19:57:52Z
- Update date including text: 2025-04-09T19:57:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/766",
    "number": "766",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000598",
        "district": "42",
        "firstName": "Robert",
        "fullName": "Rep. Garcia, Robert [D-CA-42]",
        "lastName": "Garcia",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SEWER Act",
    "type": "HR",
    "updateDate": "2025-04-09T19:57:52Z",
    "updateDateIncludingText": "2025-04-09T19:57:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NE"
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
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr766ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 766\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Garcia of California (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to require the Secretary to award grants, contracts, or cooperative agreements to eligible entities to establish, maintain, or improve activities related to the detection and monitoring of infectious diseases through wastewater for public health emergency preparedness and response purposes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Surveilling Effluent Water for Epidemic Response Act or the SEWER Act .\n#### 2. National Wastewater Surveillance System\n##### (a) In general\nSubtitle C of title XXVIII of the Public Health Service Act ( 42 U.S.C. 300hh\u201331 et seq. ) is amended by adding at the end the following:\n2827. National Wastewater Surveillance System (a) National wastewater surveillance system The Secretary, acting through the Director of the Centers for Disease Control and Prevention, and in coordination with Federal departments and agencies and relevant State and local departments and agencies, shall expand, intensify, and coordinate the activities of the National Wastewater Surveillance System to detect and monitor pathogens in wastewater, such as SARS\u2013CoV\u20132, influenza, mpox, dengue, West Nile virus, and respiratory syncytial virus. (b) Authorization of appropriations To carry out this section, there is authorized to be appropriated $150,000,000 for each of fiscal years 2026 through 2030, to remain available until expended. .\n##### (b) Rule of construction\nNothing in the amendment made by subsection (a) shall be construed as requiring a wastewater utility or service provider to comply with a request for wastewater surveillance.",
      "versionDate": "2025-01-28",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-03-27T15:26:46Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-03-27T15:26:32Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-27T15:26:38Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-03-27T15:26:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-01T14:34:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr766",
          "measure-number": "766",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr766v00",
            "update-date": "2025-04-09"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Surveilling Effluent Water for Epidemic Response Act or the SEWER Act</strong></p><p>This bill provides statutory authority for the Centers for Disease Control and Prevention (CDC) National Wastewater Surveillance System (NWSS) program, which detects and monitors pathogens in wastewater. It requires the CDC to expand and intensify the activities of the NWSS, including with respect to SARS-CoV-2\u00a0(the virus that causes\u00a0COVID-19), influenza, mpox, dengue, West Nile virus, and respiratory syncytial virus (RSV).\u00a0</p><p>The\u00a0NWSS\u00a0provides funding and guidance to public health departments for wastewater surveillance activities.\u00a0Under the NWSS, health departments and other partners coordinate on wastewater\u00a0surveillance at sampling sites and share data with the CDC. The NWSS was initially\u00a0implemented\u00a0to monitor\u00a0SARS-CoV-2\u00a0and has since expanded to include influenza A, avian influenza A,\u00a0mpox, and RSV. \u00a0 \u00a0\u00a0</p>"
        },
        "title": "SEWER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr766.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Surveilling Effluent Water for Epidemic Response Act or the SEWER Act</strong></p><p>This bill provides statutory authority for the Centers for Disease Control and Prevention (CDC) National Wastewater Surveillance System (NWSS) program, which detects and monitors pathogens in wastewater. It requires the CDC to expand and intensify the activities of the NWSS, including with respect to SARS-CoV-2\u00a0(the virus that causes\u00a0COVID-19), influenza, mpox, dengue, West Nile virus, and respiratory syncytial virus (RSV).\u00a0</p><p>The\u00a0NWSS\u00a0provides funding and guidance to public health departments for wastewater surveillance activities.\u00a0Under the NWSS, health departments and other partners coordinate on wastewater\u00a0surveillance at sampling sites and share data with the CDC. The NWSS was initially\u00a0implemented\u00a0to monitor\u00a0SARS-CoV-2\u00a0and has since expanded to include influenza A, avian influenza A,\u00a0mpox, and RSV. \u00a0 \u00a0\u00a0</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr766"
    },
    "title": "SEWER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Surveilling Effluent Water for Epidemic Response Act or the SEWER Act</strong></p><p>This bill provides statutory authority for the Centers for Disease Control and Prevention (CDC) National Wastewater Surveillance System (NWSS) program, which detects and monitors pathogens in wastewater. It requires the CDC to expand and intensify the activities of the NWSS, including with respect to SARS-CoV-2\u00a0(the virus that causes\u00a0COVID-19), influenza, mpox, dengue, West Nile virus, and respiratory syncytial virus (RSV).\u00a0</p><p>The\u00a0NWSS\u00a0provides funding and guidance to public health departments for wastewater surveillance activities.\u00a0Under the NWSS, health departments and other partners coordinate on wastewater\u00a0surveillance at sampling sites and share data with the CDC. The NWSS was initially\u00a0implemented\u00a0to monitor\u00a0SARS-CoV-2\u00a0and has since expanded to include influenza A, avian influenza A,\u00a0mpox, and RSV. \u00a0 \u00a0\u00a0</p>",
      "updateDate": "2025-04-09",
      "versionCode": "id119hr766"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr766ih.xml"
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
      "title": "SEWER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEWER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Surveilling Effluent Water for Epidemic Response Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to require the Secretary to award grants, contracts, or cooperative agreements to eligible entities to establish, maintain, or improve activities related to the detection and monitoring of infectious diseases through wastewater for public health emergency preparedness and response purposes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:33Z"
    }
  ]
}
```
