# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/57?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/57
- Title: Ending Catch and Release Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 57
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-11-21T12:04:11Z
- Update date including text: 2025-11-21T12:04:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/57",
    "number": "57",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Ending Catch and Release Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-21T12:04:11Z",
    "updateDateIncludingText": "2025-11-21T12:04:11Z"
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
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
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
          "date": "2025-01-03T16:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "SC"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr57ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 57\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Ms. Mace ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act with respect to the parole or release of an asylum applicant, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ending Catch and Release Act of 2025 .\n#### 2. Inspection of applicants for admission\nSection 235(b) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b) ) is amended by\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i)\u2014\n**(I)**\nby striking section 212(a)(6)(C) and inserting section 212(a)(6)(A), 212(a)(6)(C), or ; and\n**(II)**\nby striking the period at the end and inserting . The Secretary may not parole or otherwise release the alien into the United States. ; and\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nby striking section 212(a)(6)(C) and inserting section 212(a)(6)(A), 212(a)(6)(C), or ; and\n**(II)**\nby striking the period at the end and inserting . The Secretary may not parole or otherwise release the alien into the United States. ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking Attorney General and inserting Secretary ;\n**(ii)**\nin clause (ii), by striking the alien shall be detained for further consideration of the application for asylum and inserting the alien shall either be detained for further consideration of the application for asylum by an immigration judge or if the alien arrived on land from a foreign territory contiguous to the United States, be returned to that territory for further consideration of the application for asylum by an immigration judge. The Secretary may not parole or otherwise release the alien into the United States ;\n**(iii)**\nin clause (iii)\u2014\n**(I)**\nin subclause (I), by striking the period at the end and adding . The Secretary shall remove the alien within 72 hours. If the alien cannot be removed, the alien shall be detained until removed. The Secretary may not parole or otherwise release the alien into the United States. ;\n**(II)**\nin subclause (II), by striking has not and inserting has or has not ; and\n**(III)**\nin subclause (IV), by striking the period at the end and inserting . The Secretary may not parole or otherwise release the alien into the United States. ; and\n**(iv)**\nin clause (v), by striking there is a significant possibility, taking into account the credibility of the statements made by the alien in support of the alien's claim and such other facts as are known to the officer, that the alien could establish eligibility for asylum under section 208 and inserting it is more likely than not that the alien will be able to establish eligibility for asylum under section 208 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking and (C) ; and\n**(ii)**\nby striking the alien shall be detained for a proceeding under section 240. and inserting the alien shall be either detained for a proceeding under section 240 or if the alien arrived on land from a foreign territory contiguous to the United States, be returned to that territory pending a proceeding under section 240. The Secretary may not parole or otherwise release the alien into the United States. ; and\n**(B)**\nby striking subparagraph (C).",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-06-10T16:02:38Z"
          },
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-10T16:01:42Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-06-10T16:00:04Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-10T15:58:53Z"
          },
          {
            "name": "Refugees, asylum, displaced persons",
            "updateDate": "2025-06-10T15:59:13Z"
          },
          {
            "name": "Specialized courts",
            "updateDate": "2025-06-10T16:01:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-01-31T14:19:53Z"
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
          "measure-id": "id119hr57",
          "measure-number": "57",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr57v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ending Catch and Release Act of 2025</strong></p><p>This bill changes the treatment of certain non-U.S. nationals (<em>aliens</em> under federal law) without lawful immigration status, including by prohibiting the release of asylum seekers into the United States while their cases are pending.</p><p>The Department of Homeland Security (DHS) may not (with some exceptions) release an individual who is not clearly entitled to admission into the United States while the individual's case is pending, even if the individual is an asylum seeker. DHS may instead detain the individual or return the individual to a neighboring country in certain situations.</p><p>The bill also expands expedited removal from the United States (i.e., removal without further hearing or review) to include individuals present in the United States without being admitted, with certain exceptions. Under current law, individuals are subject to expedited removal if they lack proper documentation or obtained an immigration benefit through fraud; such individuals are still subject to expedited removal under the bill.</p><p>The bill also modifies the standard for establishing a credible fear of persecution to avoid expedited removal. Generally, an asylum seeker may avoid expedited removal if an asylum officer finds such a credible fear. Under this bill, an officer may find credible fear if it is more likely than not the individual can establish their eligibility for asylum, whereas under current law, the officer may find credible fear if there is a <em>significant possibility</em> that the individual can establish their eligibility.</p>"
        },
        "title": "Ending Catch and Release Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr57.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending Catch and Release Act of 2025</strong></p><p>This bill changes the treatment of certain non-U.S. nationals (<em>aliens</em> under federal law) without lawful immigration status, including by prohibiting the release of asylum seekers into the United States while their cases are pending.</p><p>The Department of Homeland Security (DHS) may not (with some exceptions) release an individual who is not clearly entitled to admission into the United States while the individual's case is pending, even if the individual is an asylum seeker. DHS may instead detain the individual or return the individual to a neighboring country in certain situations.</p><p>The bill also expands expedited removal from the United States (i.e., removal without further hearing or review) to include individuals present in the United States without being admitted, with certain exceptions. Under current law, individuals are subject to expedited removal if they lack proper documentation or obtained an immigration benefit through fraud; such individuals are still subject to expedited removal under the bill.</p><p>The bill also modifies the standard for establishing a credible fear of persecution to avoid expedited removal. Generally, an asylum seeker may avoid expedited removal if an asylum officer finds such a credible fear. Under this bill, an officer may find credible fear if it is more likely than not the individual can establish their eligibility for asylum, whereas under current law, the officer may find credible fear if there is a <em>significant possibility</em> that the individual can establish their eligibility.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr57"
    },
    "title": "Ending Catch and Release Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ending Catch and Release Act of 2025</strong></p><p>This bill changes the treatment of certain non-U.S. nationals (<em>aliens</em> under federal law) without lawful immigration status, including by prohibiting the release of asylum seekers into the United States while their cases are pending.</p><p>The Department of Homeland Security (DHS) may not (with some exceptions) release an individual who is not clearly entitled to admission into the United States while the individual's case is pending, even if the individual is an asylum seeker. DHS may instead detain the individual or return the individual to a neighboring country in certain situations.</p><p>The bill also expands expedited removal from the United States (i.e., removal without further hearing or review) to include individuals present in the United States without being admitted, with certain exceptions. Under current law, individuals are subject to expedited removal if they lack proper documentation or obtained an immigration benefit through fraud; such individuals are still subject to expedited removal under the bill.</p><p>The bill also modifies the standard for establishing a credible fear of persecution to avoid expedited removal. Generally, an asylum seeker may avoid expedited removal if an asylum officer finds such a credible fear. Under this bill, an officer may find credible fear if it is more likely than not the individual can establish their eligibility for asylum, whereas under current law, the officer may find credible fear if there is a <em>significant possibility</em> that the individual can establish their eligibility.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hr57"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr57ih.xml"
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
      "title": "Ending Catch and Release Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ending Catch and Release Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act with respect to the parole or release of an asylum applicant, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T06:18:25Z"
    }
  ]
}
```
