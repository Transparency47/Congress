# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/389
- Title: Setting Consumer Standards for Lithium-Ion Batteries Act
- Congress: 119
- Bill type: S
- Bill number: 389
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2026-02-04T04:11:38Z
- Update date including text: 2026-02-04T04:11:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-50.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-50.
- 2025-07-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 133.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-50.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-50.
- 2025-07-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 133.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/389",
    "number": "389",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Setting Consumer Standards for Lithium-Ion Batteries Act",
    "type": "S",
    "updateDate": "2026-02-04T04:11:38Z",
    "updateDateIncludingText": "2026-02-04T04:11:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 133.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-50.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-50.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
        "item": [
          {
            "date": "2025-07-29T20:58:39Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-04T19:42:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s389is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 389\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mrs. Gillibrand (for herself, Mrs. Blackburn , Mrs. Fischer , and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish consumer standards for lithium-ion batteries.\n#### 1. Short title\nThis Act may be cited as the Setting Consumer Standards for Lithium-Ion Batteries Act .\n#### 2. Consumer product safety standard for certain batteries\n##### (a) Consumer product safety standard required\nNot later than 180 days after the date of the enactment of this Act, the Consumer Product Safety Commission (referred to in this section as the Commission ) shall promulgate, under section 553 of title 5, United States Code, the provisions of ANSI/CAN/UL 2271\u2013Standard for Batteries for Use in Light Electric Vehicle Applications, ANSI/CAN/UL 2849\u2013Standard for Safety for Electrical Systems for eBikes, and ANSI/CA/UL 2272\u2013Standard for Electrical Systems for Personal E-Mobility Devices, as in effect on the date of enactment of this Act, as final consumer product safety standards.\n##### (b) Consumer Product Safety Commission determination of scope\nIn adopting the standards under subsection (a), the Commission shall limit the application of such standards to consumer products as defined in section 3(a)(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ).\n##### (c) Revision of voluntary standards\n**(1) Notice to Commission**\nIf the provisions of ANSI/CAN/UL 2271\u2013Standard for Batteries for Use in Light Electric Vehicle Applications, ANSI/CAN/UL 2849\u2013Standard for Safety for Electrical Systems for eBikes, or ANSI/CAN/UL 2272\u2013Standard for Electrical Systems for Personal E-Mobility Devices, are revised following the enactment of this Act, the organization that revised the requirements of such standard shall notify the Commission after the final approval of the revision.\n**(2) Treatment of revision**\nThe revised voluntary standard shall be considered to be a consumer product safety standard issued by the Commission under section 9 of the Consumer Product Safety Act ( 15 U.S.C. 2058 ), effective 180 days after the date on which the organization notifies the Commission (or such later date specified by the Commission in the Federal Register) unless, within 90 days after receiving that notice, the Commission notifies the organization that it has determined that the proposed revision, in whole or in part, does not improve the safety of the consumer product covered by the standard and that the Commission is retaining the existing consumer product safety standard.\n##### (d) Treatment of standard\nA standard promulgated under this section, including a revision of such standard adopted by the Commission, shall be treated as a consumer product safety rule promulgated under section 9 of the Consumer Product Safety Act ( 15 U.S.C. 2058 ).\n##### (e) Report to Congress\n**(1) In general**\nNot later than 5 years after the date of enactment of this Act, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report regarding fires, explosions, and other hazards relating to lithium-ion batteries used in micromobility products during the period beginning on the date of enactment of this Act and ending on the report date.\n**(2) Content**\nThe report required by paragraph (1) shall describe, at a minimum\u2014\n**(A)**\nthe source of the information that was provided to the Commission regarding the fire, explosion, or other hazard;\n**(B)**\nthe make and model of the lithium-ion battery and micromobility product that resulted in a fire, explosion, or other hazard, if known;\n**(C)**\nwhether a lithium-ion battery involved in a fire, explosion, or other hazard complied with the standard required by this section, if known; and\n**(D)**\nif known, the manufacturer and country of manufacture of a lithium-ion battery that resulted in a fire, explosion, or other hazard.",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s389rs.xml",
      "text": "II\nCalendar No. 133\n119th CONGRESS\n1st Session\nS. 389\n[Report No. 119\u201350]\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mrs. Gillibrand (for herself, Mrs. Blackburn , Mrs. Fischer , and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nJuly 29, 2025 Reported by Mr. Cruz , with an amendment Insert the part printed in italic\nA BILL\nTo establish consumer standards for lithium-ion batteries.\n#### 1. Short title\nThis Act may be cited as the Setting Consumer Standards for Lithium-Ion Batteries Act .\n#### 2. Consumer product safety standard for certain batteries\n##### (a) Consumer product safety standard required\nNot later than 180 days after the date of the enactment of this Act, the Consumer Product Safety Commission (referred to in this section as the Commission ) shall promulgate, under section 553 of title 5, United States Code, the provisions of ANSI/CAN/UL 2271\u2013Standard for Batteries for Use in Light Electric Vehicle Applications, ANSI/CAN/UL 2849\u2013Standard for Safety for Electrical Systems for eBikes, and ANSI/CA N /UL 2272\u2013Standard for Electrical Systems for Personal E-Mobility Devices, as in effect on the date of enactment of this Act, as final consumer product safety standards.\n##### (b) Consumer Product Safety Commission determination of scope\nIn adopting the standards under subsection (a), the Commission shall limit the application of such standards to consumer products as defined in section 3(a)(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ).\n##### (c) Revision of voluntary standards\n**(1) Notice to Commission**\nIf the provisions of ANSI/CAN/UL 2271\u2013Standard for Batteries for Use in Light Electric Vehicle Applications, ANSI/CAN/UL 2849\u2013Standard for Safety for Electrical Systems for eBikes, or ANSI/CAN/UL 2272\u2013Standard for Electrical Systems for Personal E-Mobility Devices, are revised following the enactment of this Act, the organization that revised the requirements of such standard shall notify the Commission after the final approval of the revision.\n**(2) Treatment of revision**\nThe revised voluntary standard shall be considered to be a consumer product safety standard issued by the Commission under section 9 of the Consumer Product Safety Act ( 15 U.S.C. 2058 ), effective 180 days after the date on which the organization notifies the Commission (or such later date specified by the Commission in the Federal Register) unless, within 90 days after receiving that notice, the Commission notifies the organization that it has determined that the proposed revision, in whole or in part, does not improve the safety of the consumer product covered by the standard and that the Commission is retaining the existing consumer product safety standard.\n##### (d) Treatment of standard\nA standard promulgated under this section, including a revision of such standard adopted by the Commission, shall be treated as a consumer product safety rule promulgated under section 9 of the Consumer Product Safety Act ( 15 U.S.C. 2058 ).\n##### (e) Report to Congress\n**(1) In general**\nNot later than 5 years after the date of enactment of this Act, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives, a report regarding fires, explosions, and other hazards relating to lithium-ion batteries used in micromobility products during the period beginning on the date of enactment of this Act and ending on the report date.\n**(2) Content**\nThe report required by paragraph (1) shall describe, at a minimum\u2014\n**(A)**\nthe source of the information that was provided to the Commission regarding the fire, explosion, or other hazard;\n**(B)**\nthe make and model of the lithium-ion battery and micromobility product that resulted in a fire, explosion, or other hazard, if known;\n**(C)**\nwhether a lithium-ion battery involved in a fire, explosion, or other hazard complied with the standard required by this section, if known; and\n**(D)**\nif known, the manufacturer and country of manufacture of a lithium-ion battery that resulted in a fire, explosion, or other hazard.",
      "versionDate": "2025-07-29",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
            "name": "Consumer affairs",
            "updateDate": "2025-04-23T13:32:11Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2025-04-23T13:32:11Z"
          },
          {
            "name": "Pedestrians and bicycling",
            "updateDate": "2025-04-23T13:32:11Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2025-04-23T13:32:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-05T15:35:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s389",
          "measure-number": "389",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s389v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Setting Consumer Standards for Lithium-Ion Batteries Act</strong></p><p>This bill requires the Consumer Product Safety Commission to issue a final consumer product safety rule for rechargeable lithium-ion batteries used in\u00a0micromobility devices, such as electric bikes and electric scooters.</p><p>Specifically, the rule must require manufacturers and distributors of\u00a0such products to comply with the applicable\u00a0safety standards jointly\u00a0established by the American National Standards Institute, the Standards Council of Canada, and UL Solutions Inc.</p>"
        },
        "title": "Setting Consumer Standards for Lithium-Ion Batteries Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s389.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Setting Consumer Standards for Lithium-Ion Batteries Act</strong></p><p>This bill requires the Consumer Product Safety Commission to issue a final consumer product safety rule for rechargeable lithium-ion batteries used in\u00a0micromobility devices, such as electric bikes and electric scooters.</p><p>Specifically, the rule must require manufacturers and distributors of\u00a0such products to comply with the applicable\u00a0safety standards jointly\u00a0established by the American National Standards Institute, the Standards Council of Canada, and UL Solutions Inc.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119s389"
    },
    "title": "Setting Consumer Standards for Lithium-Ion Batteries Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Setting Consumer Standards for Lithium-Ion Batteries Act</strong></p><p>This bill requires the Consumer Product Safety Commission to issue a final consumer product safety rule for rechargeable lithium-ion batteries used in\u00a0micromobility devices, such as electric bikes and electric scooters.</p><p>Specifically, the rule must require manufacturers and distributors of\u00a0such products to comply with the applicable\u00a0safety standards jointly\u00a0established by the American National Standards Institute, the Standards Council of Canada, and UL Solutions Inc.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119s389"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s389is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s389rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Setting Consumer Standards for Lithium-Ion Batteries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T11:03:12Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Setting Consumer Standards for Lithium-Ion Batteries Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Setting Consumer Standards for Lithium-Ion Batteries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish consumer standards for lithium-ion batteries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:31Z"
    }
  ]
}
```
