# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1272?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1272
- Title: Trade Review Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1272
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-04-15T14:40:22Z
- Update date including text: 2026-04-15T14:40:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S2173-2174)
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S2173-2174)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1272",
    "number": "1272",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Trade Review Act of 2025",
    "type": "S",
    "updateDate": "2026-04-15T14:40:22Z",
    "updateDateIncludingText": "2026-04-15T14:40:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S2173-2174)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
        "item": {
          "date": "2025-04-03T14:54:46Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "IA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "KS"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "AK"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "VA"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "KY"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CO"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "NC"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "VT"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "IN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "DE"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-04",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1272is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1272\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Ms. Cantwell (for herself, Mr. Grassley , Mr. Moran , Ms. Klobuchar , Ms. Murkowski , Mr. Warner , Mr. McConnell , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for notification to, and review by, Congress with respect to the imposition of duties.\n#### 1. Short title\nThis Act may be cited as the Trade Review Act of 2025 .\n#### 2. Review by Congress of imposition of duties\n##### (a) In general\nChapter 5 of title I of the Trade Act of 1974 ( 19 U.S.C. 2191 et seq. ) is amended by adding at the end the following:\n155. Review of imposition of duties (a) Notification requirement Not later than 48 hours after imposing or increasing a duty with respect to an article imported into the United States, the President shall submit to Congress a notification of the imposition of or increase in the duty that includes\u2014 (1) an explanation of the reasoning for imposing or increasing the duty; and (2) an assessment of the potential impact of imposing or increasing the duty on United States businesses and consumers. (b) Expiration of duties; extension by Congress Any duty on an article imported into the United States shall remain in effect for a period of not more than 60 days, unless there is enacted into law a joint resolution of approval with respect to the duty under subsection (e). (c) Disapproval by Congress If a joint resolution of disapproval with respect to a duty is enacted into law under subsection (e), the duty shall cease to have force or effect. (d) Exclusion of antidumping and countervailing duties This section does not apply with respect to antidumping and countervailing duties imposed under title VII of the Tariff Act of 1930 ( 19 U.S.C. 1671 et seq. ). (e) Joint resolutions (1) Definitions In this section: (A) Joint resolution of approval The term joint resolution of approval means a joint resolution the sole matter after the resolving clause of which is as follows: That Congress approves the duty imposed with respect to ___, notice of which was submitted to Congress on ______. , with the first blank space being filled with a description of the article and the second blank space being filled with the date of the notification under subsection (a). (B) Joint resolution of disapproval The term joint resolution of disapproval means a joint resolution the sole matter after the resolving clause of which is as follows: That Congress disapproves the duty imposed with respect to ___, notice of which was submitted to Congress on ______. , with the first blank space being filled with a description of the article and the second blank space being filled with the date of the notification under subsection (a). (2) Introduction (A) Joint resolution of approval A joint resolution of approval may be introduced in either House of Congress by any Member during the 60-day period described in subsection (b). (B) Joint resolution of disapproval A joint resolution of disapproval may be introduced in either House of Congress by any Member at any time after the submission of a notification under subsection (a). (3) Expedited procedures The provisions of subsections (b) through (f) of section 152 ( 19 U.S.C. 2192 ) apply to a joint resolution of approval or joint resolution of disapproval to the same extent that such subsections apply to joint resolutions under section 152. (4) Rules of the Senate and the House of Representatives This subsection is enacted by Congress\u2014 (A) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in that House in the case of a joint resolution of approval, and supersedes other rules only to the extent that it is inconsistent with such rules; and (B) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. .\n##### (b) Clerical amendment\nThe table of contents for the Trade Act of 1974 is amended by inserting after the item relating to section 154 the following:\nSec. 155. Review of imposition of duties. .",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-07",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2665",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Trade Review Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-14T15:22:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119s1272",
          "measure-number": "1272",
          "measure-type": "s",
          "orig-publish-date": "2025-04-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1272v00",
            "update-date": "2026-04-15"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Trade Review Act of 2025</strong></p><p>This bill requires congressional notification and review of new or increased duties (i.e., tariffs) imposed by the President on articles\u00a0imported into the United States.\u00a0</p><p>Specifically, the President must notify Congress within 48 hours of imposing or increasing a duty on articles imported into the United States. This notification must include (1) the rationale for imposing or increasing the duty, and (2) an assessment of the duty's potential impact on U.S. businesses and consumers. The bill limits the duration of a duty to 60 days, unless\u00a0a joint resolution of approval is enacted into law.</p><p>A duty shall cease to have force or effect if a joint resolution of disapproval is enacted into law.</p>"
        },
        "title": "Trade Review Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1272.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Trade Review Act of 2025</strong></p><p>This bill requires congressional notification and review of new or increased duties (i.e., tariffs) imposed by the President on articles\u00a0imported into the United States.\u00a0</p><p>Specifically, the President must notify Congress within 48 hours of imposing or increasing a duty on articles imported into the United States. This notification must include (1) the rationale for imposing or increasing the duty, and (2) an assessment of the duty's potential impact on U.S. businesses and consumers. The bill limits the duration of a duty to 60 days, unless\u00a0a joint resolution of approval is enacted into law.</p><p>A duty shall cease to have force or effect if a joint resolution of disapproval is enacted into law.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s1272"
    },
    "title": "Trade Review Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Trade Review Act of 2025</strong></p><p>This bill requires congressional notification and review of new or increased duties (i.e., tariffs) imposed by the President on articles\u00a0imported into the United States.\u00a0</p><p>Specifically, the President must notify Congress within 48 hours of imposing or increasing a duty on articles imported into the United States. This notification must include (1) the rationale for imposing or increasing the duty, and (2) an assessment of the duty's potential impact on U.S. businesses and consumers. The bill limits the duration of a duty to 60 days, unless\u00a0a joint resolution of approval is enacted into law.</p><p>A duty shall cease to have force or effect if a joint resolution of disapproval is enacted into law.</p>",
      "updateDate": "2026-04-15",
      "versionCode": "id119s1272"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1272is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-04-15T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Trade Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-15T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for notification to, and review by, Congress with respect to the imposition of duties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-15T04:19:02Z"
    }
  ]
}
```
