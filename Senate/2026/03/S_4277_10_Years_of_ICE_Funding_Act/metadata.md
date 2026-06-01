# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4277?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4277
- Title: 10 Years of ICE Funding Act
- Congress: 119
- Bill type: S
- Bill number: 4277
- Origin chamber: Senate
- Introduced date: 2026-03-27
- Update date: 2026-04-13T15:07:02Z
- Update date including text: 2026-04-13T15:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-27: Introduced in Senate
- 2026-03-27 - IntroReferral: Introduced in Senate
- 2026-03-27 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-04-02 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 368.
- Latest action: 2026-03-27: Introduced in Senate

## Actions

- 2026-03-27 - IntroReferral: Introduced in Senate
- 2026-03-27 - Calendars: Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.
- 2026-04-02 - Calendars: Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 368.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4277",
    "number": "4277",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "10 Years of ICE Funding Act",
    "type": "S",
    "updateDate": "2026-04-13T15:07:02Z",
    "updateDateIncludingText": "2026-04-13T15:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read the second time. Placed on Senate Legislative Calendar under General Orders. Calendar No. 368.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Introduced in the Senate. Read the first time. Placed on Senate Legislative Calendar under Read the First Time.",
      "type": "Calendars"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-27",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "MO"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4277pcs.xml",
      "text": "II\nCalendar No. 368\n119th CONGRESS\n2d Session\nS. 4277\nIN THE SENATE OF THE UNITED STATES\nMarch 27 (legislative day, March 26), 2026 Mr. Schmitt (for himself, Mr. Hawley , and Mr. Moreno ) introduced the following bill; which was read the first time\nApril 2, 2026 Read the second time and placed on the calendar\nA BILL\nTo make appropriations for U.S. Immigration and Customs Enforcement.\n#### 1. Short title\nThis Act may be cited as the 10 Years of ICE Funding Act .\n#### 2. U.S. Immigration and Customs Enforcement\n##### (a) Operations and support\nFor necessary expenses of U.S. Immigration and Customs Enforcement for operations and support, including for the purchase and lease of up to 3,790 police-type vehicles (of which 2,350 vehicles shall be replacement vehicles only), for overseas vetted units, and for maintenance, minor construction, and minor leasehold improvements at owned and leased facilities, $100,363,620,000.\n##### (b) Procurement, construction, and improvements\nFor necessary expenses of U.S. Immigration and Customs Enforcement for procurement, construction, and improvements, including acquisition of necessary additional real property and facilities, construction and ongoing maintenance, facility improvements, equipment, and related expenses, $5,000,000,000.\n##### (c) Availability\nAmounts appropriated under subsections (a) and (b) shall remain available until September 30, 2036.\n##### (d) Rule of construction\nAmounts appropriated under subsections (a) and (b) shall remain available for obligation notwithstanding section 501 of the Department of Homeland Security Appropriations Act, 2026, or any other provision of law limiting the period of availability of such amounts.",
      "versionDate": "2026-04-02",
      "versionType": "Placed on Calendar Senate"
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
        "name": "Immigration",
        "updateDate": "2026-04-09T17:53:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-27",
    "originChamber": "Senate",
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
          "measure-id": "id119s4277",
          "measure-number": "4277",
          "measure-type": "s",
          "orig-publish-date": "2026-03-27",
          "originChamber": "SENATE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4277v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2026-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>10 Years of ICE Funding Act</strong></p><p>This bill provides appropriations for U.S. Immigration and Customs Enforcement (ICE) through FY2036.</p><p>Specifically, the bill provides specified appropriations to ICE for operations and support, including for the purchase and lease of police-type vehicles, for overseas vetted units, and for maintenance, minor construction, and minor leasehold improvements at owned and leased facilities.</p><p>The bill also provides appropriations to ICE for procurement, construction, and improvements, including for acquisition of necessary additional real property and facilities, construction and ongoing maintenance, facility improvements, equipment, and related expenses.</p><p>The appropriations provided to ICE by this bill are available until September 30, 2036.\u00a0</p>"
        },
        "title": "10 Years of ICE Funding Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4277.xml",
    "summary": {
      "actionDate": "2026-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>10 Years of ICE Funding Act</strong></p><p>This bill provides appropriations for U.S. Immigration and Customs Enforcement (ICE) through FY2036.</p><p>Specifically, the bill provides specified appropriations to ICE for operations and support, including for the purchase and lease of police-type vehicles, for overseas vetted units, and for maintenance, minor construction, and minor leasehold improvements at owned and leased facilities.</p><p>The bill also provides appropriations to ICE for procurement, construction, and improvements, including for acquisition of necessary additional real property and facilities, construction and ongoing maintenance, facility improvements, equipment, and related expenses.</p><p>The appropriations provided to ICE by this bill are available until September 30, 2036.\u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s4277"
    },
    "title": "10 Years of ICE Funding Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>10 Years of ICE Funding Act</strong></p><p>This bill provides appropriations for U.S. Immigration and Customs Enforcement (ICE) through FY2036.</p><p>Specifically, the bill provides specified appropriations to ICE for operations and support, including for the purchase and lease of police-type vehicles, for overseas vetted units, and for maintenance, minor construction, and minor leasehold improvements at owned and leased facilities.</p><p>The bill also provides appropriations to ICE for procurement, construction, and improvements, including for acquisition of necessary additional real property and facilities, construction and ongoing maintenance, facility improvements, equipment, and related expenses.</p><p>The appropriations provided to ICE by this bill are available until September 30, 2036.\u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119s4277"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4277pcs.xml"
        }
      ],
      "type": "Placed on Calendar Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "10 Years of ICE Funding Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "PCS",
      "billTextVersionName": "Placed on Calendar Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "10 Years of ICE Funding Act",
      "titleType": "Short Title(s) from PCS (Placed on Senate Calendar) bill text",
      "titleTypeCode": "152",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "title": "A bill to make appropriations for U.S. Immigration and Customs Enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-27T10:56:20Z"
    }
  ]
}
```
