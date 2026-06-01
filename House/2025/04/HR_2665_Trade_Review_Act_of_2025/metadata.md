# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2665
- Title: Trade Review Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2665
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-04-15T15:59:31Z
- Update date including text: 2026-04-15T15:59:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-07 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2665",
    "number": "2665",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Trade Review Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T15:59:31Z",
    "updateDateIncludingText": "2026-04-15T15:59:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-07T16:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CO"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "WA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2665ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2665\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Bacon (for himself, Mr. Hurd of Colorado , Mr. Gottheimer , and Mr. Meeks ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for notification to, and review by, Congress with respect to the imposition of duties.\n#### 1. Short title\nThis Act may be cited as the Trade Review Act of 2025 .\n#### 2. Review by Congress of imposition of duties\n##### (a) In general\nChapter 5 of title I of the Trade Act of 1974 ( 19 U.S.C. 2191 et seq. ) is amended by adding at the end the following:\n155. Review of imposition of duties (a) Notification requirement Not later than 48 hours after imposing or increasing a duty with respect to an article imported into the United States, the President shall submit to Congress a notification of the imposition of or increase in the duty that includes\u2014 (1) an explanation of the reasoning for imposing or increasing the duty; and (2) an assessment of the potential impact of imposing or increasing the duty on United States businesses and consumers. (b) Expiration of duties; extension by Congress Any duty on an article imported into the United States shall remain in effect for a period of not more than 60 days, unless there is enacted into law a joint resolution of approval with respect to the duty under subsection (e). (c) Disapproval by Congress If a joint resolution of disapproval with respect to a duty is enacted into law under subsection (e), the duty shall cease to have force or effect. (d) Exclusion of antidumping and countervailing duties This section does not apply with respect to antidumping and countervailing duties imposed under title VII of the Tariff Act of 1930 ( 19 U.S.C. 1671 et seq. ). (e) Joint resolutions (1) Definitions In this section: (A) Joint resolution of approval The term joint resolution of approval means a joint resolution the sole matter after the resolving clause of which is as follows: That Congress approves the duty imposed with respect to ___, notice of which was submitted to Congress on ______. , with the first blank space being filled with a description of the article and the second blank space being filled with the date of the notification under subsection (a). (B) Joint resolution of disapproval The term joint resolution of disapproval means a joint resolution the sole matter after the resolving clause of which is as follows: That Congress disapproves the duty imposed with respect to ___, notice of which was submitted to Congress on ______. , with the first blank space being filled with a description of the article and the second blank space being filled with the date of the notification under subsection (a). (2) Introduction (A) Joint resolution of approval A joint resolution of approval may be introduced in either House of Congress by any Member during the 60-day period described in subsection (b). (B) Joint resolution of disapproval A joint resolution of disapproval may be introduced in either House of Congress by any Member at any time after the submission of a notification under subsection (a). (3) Expedited procedures The provisions of subsections (b) through (f) of section 152 ( 19 U.S.C. 2192 ) apply to a joint resolution of approval or joint resolution of disapproval to the same extent that such subsections apply to joint resolutions under section 152. (4) Rules of the Senate and the House of Representatives This subsection is enacted by Congress\u2014 (A) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of a joint resolution of approval, and supersedes other rules only to the extent that it is inconsistent with such rules; and (B) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. .\n##### (b) Clerical amendment\nThe table of contents for the Trade Act of 1974 is amended by inserting after the item relating to section 154 the following:\nSec. 155. Review of imposition of duties. .",
      "versionDate": "2025-04-07",
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
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S2173-2174)"
      },
      "number": "1272",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Trade Review Act of 2025",
      "type": "S"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-14T15:20:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2665",
          "measure-number": "2665",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2665v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Trade Review Act of 2025</strong></p><p>This bill requires congressional notification and review of new or increased duties (i.e., tariffs) imposed by the President on articles\u00a0imported into the United States.\u00a0</p><p>Specifically, the President must notify Congress within 48 hours of imposing or increasing a duty on articles imported into the United States. This notification must include (1) the rationale for imposing or increasing the duty, and (2) an assessment of the duty's potential impact on U.S. businesses and consumers. The bill limits the duration of a duty to 60 days, unless\u00a0a joint resolution of approval is enacted into law.</p><p>A duty shall cease to have force or effect if a joint resolution of disapproval is enacted into law.</p>"
        },
        "title": "Trade Review Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2665.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Trade Review Act of 2025</strong></p><p>This bill requires congressional notification and review of new or increased duties (i.e., tariffs) imposed by the President on articles\u00a0imported into the United States.\u00a0</p><p>Specifically, the President must notify Congress within 48 hours of imposing or increasing a duty on articles imported into the United States. This notification must include (1) the rationale for imposing or increasing the duty, and (2) an assessment of the duty's potential impact on U.S. businesses and consumers. The bill limits the duration of a duty to 60 days, unless\u00a0a joint resolution of approval is enacted into law.</p><p>A duty shall cease to have force or effect if a joint resolution of disapproval is enacted into law.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119hr2665"
    },
    "title": "Trade Review Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Trade Review Act of 2025</strong></p><p>This bill requires congressional notification and review of new or increased duties (i.e., tariffs) imposed by the President on articles\u00a0imported into the United States.\u00a0</p><p>Specifically, the President must notify Congress within 48 hours of imposing or increasing a duty on articles imported into the United States. This notification must include (1) the rationale for imposing or increasing the duty, and (2) an assessment of the duty's potential impact on U.S. businesses and consumers. The bill limits the duration of a duty to 60 days, unless\u00a0a joint resolution of approval is enacted into law.</p><p>A duty shall cease to have force or effect if a joint resolution of disapproval is enacted into law.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119hr2665"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2665ih.xml"
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
      "title": "Trade Review Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Trade Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for notification to, and review by, Congress with respect to the imposition of duties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T04:48:26Z"
    }
  ]
}
```
