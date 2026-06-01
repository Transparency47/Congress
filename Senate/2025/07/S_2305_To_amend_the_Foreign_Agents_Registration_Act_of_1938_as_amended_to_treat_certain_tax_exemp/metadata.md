# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2305?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2305
- Title: FRONT Act
- Congress: 119
- Bill type: S
- Bill number: 2305
- Origin chamber: Senate
- Introduced date: 2025-07-16
- Update date: 2025-07-31T04:23:22Z
- Update date including text: 2025-07-31T04:23:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2025-07-16: Introduced in Senate
- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-16: Introduced in Senate

## Actions

- 2025-07-16 - IntroReferral: Introduced in Senate
- 2025-07-16 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2305",
    "number": "2305",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "FRONT Act",
    "type": "S",
    "updateDate": "2025-07-31T04:23:22Z",
    "updateDateIncludingText": "2025-07-31T04:23:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T17:14:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "WV"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "MO"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2305is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2305\nIN THE SENATE OF THE UNITED STATES\nJuly 16, 2025 Mr. Budd (for himself, Mr. Justice , Mr. Hawley , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Foreign Agents Registration Act of 1938, as amended to treat certain tax-exempt organizations receiving funding from foreign principals of foreign countries of concern as agents of a foreign principal under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Registration Obligations for Nonprofit Transparency Act or the FRONT Act .\n#### 2. Coverage of certain tax-exempt organizations receiving funding from foreign principals of foreign countries of concern under Foreign Agents Registration Act\n##### (a) Coverage\nThe Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 611 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 12, 13, and 14 as sections 13, 14, and 15, respectively; and\n**(2)**\nby inserting after section 11 ( 22 U.S.C. 621 ) the following:\n12. Applicability to certain tax-exempt organizations receiving funding from foreign principals of foreign countries of concern (a) Applicability (1) In general For the purposes of this Act, an organization described in subsection (b) is an agent of a foreign principal. (2) Exceptions (A) Nonapplication of waiver for entities filing reports under Lobbying Disclosure Act of 1995 Section 3(h) shall not apply to an organization described in paragraph (1) or (2) of subsection (b) of this section. (B) Waiver for organizations soliciting funds outside United States for humanitarian assistance Section 3(d)(3) shall apply to an organization described in subsection (b) of this section notwithstanding that the organization solicits and collects funds and contributions outside of the United States. (b) Description An organization is described in this subsection if\u2014 (1) the organization is a partnership, association, corporation, organization, or any other combination of individuals described in paragraphs (3) through (6) of section 501(c) of the Internal Revenue Code of 1986 and exempt from taxation under such Code; (2) the organization receives income, money, or any other thing of value from a foreign principal of a foreign country of concern; and (3) the organization is not otherwise considered an agent of a foreign principal under section 1. (c) Definitions As used in this section: (1) The term foreign country of concern means\u2014 (A) the People's Republic of China; (B) the Democratic People's Republic of Korea; (C) the Russian Federation; (D) the Islamic Republic of Iran; (E) the Republic of Cuba; (F) the Bolivarian Republic of Venezuela; or (G) any other country determined to be a foreign country of concern by the Secretary of State. (2) The term foreign principal of a foreign country of concern includes\u2014 (A) the government of a foreign country of concern; (B) a political party of a foreign country of concern; (C) a national of a foreign country of concern; (D) a partnership, association, corporation, organization or other combination of persons organized under the laws of, or having its principal place of business in, a foreign country of concern; or (E) a partnership, association, corporation, organization or other combination of persons organized under the laws of, or having its principal place of business in, a foreign country other than a foreign country of concern that receives more than half of its funding from an entity described in subparagraphs (A) through (D). (3) The term government of a foreign country of concern includes\u2014 (A) any person or group of persons exercising sovereign de facto or de jure political jurisdiction over a foreign country of concern, or over any part of such country, and includes any subdivision of any such group and any group or agency to which such sovereign de facto or de jure authority or functions are directly or indirectly delegated; and (B) any faction or body of insurgents within a foreign country of concern, or a faction or body of insurgents recognized by a foreign country of concern, that are in another country assuming to exercise governmental authority whether such faction or body of insurgents has or has not been recognized by the United States. (4) The term political party of a foreign country of concern includes any organization or any other combination of individuals in a foreign country of concern, or any unit or branch thereof, having for an aim or purpose, or which is engaged in any activity devoted in whole or in part to, the establishment, administration, control, or acquisition of administration or control of the government of a foreign country of concern or subdivision thereof, or the furtherance or influencing of the political or public interests, policies, or relations of a government of foreign country of concern or a subdivision thereof. .\n##### (b) Modification of contents of reports\nSection 2(a) of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 612(a) ) is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nby striking Copies and inserting (A) Except as provided in subparagraph (B), copies ; and\n**(B)**\nby adding at the end the following:\n(B) In the case of an organization described in section 12(b), a statement that the registrant is an agent of a foreign principal pursuant to section 12(a)(1), copies of each written agreement, and the terms and conditions of each oral agreement, including all modifications of such agreements, or, where no contract exists, a full statement of the existing and proposed activity or activities engaged in or to be engaged in by the registrant as a direct or indirect result of receiving income, money, or any other thing of value from a foreign principal of a foreign country of concern (as defined in section 12(c)(2)), including a detailed statement of any such activity which is a political activity. ; and\n**(2)**\nin paragraph (9)\u2014\n**(A)**\nby striking Copies and inserting (A) Except as provided in subparagraph (B), copies ; and\n**(B)**\nby adding at the end the following:\n(B) In the case of an organization described in section 12(b), a statement that the registrant is an agent of a foreign principal pursuant to section 12(a)(1), copies of each written agreement and the terms and conditions of each oral agreement, including all modifications of such agreements, or, where no contract exists, a full statement of the existing and proposed activity or activities engaged in or to be engaged in by the registrant as a direct or indirect result of receiving income, money, or any other thing of value from a foreign principal of a foreign country of concern (as defined in section 12(a)(1)) or for any person other than a foreign principal any activities which require his registration hereunder. .\n##### (c) Effective date\nThe amendments made by this section shall take effect 30 days after the date of the enactment of this Act.",
      "versionDate": "2025-07-16",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2305is.xml"
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
      "title": "FRONT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FRONT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Foreign Registration Obligations for Nonprofit Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Foreign Agents Registration Act of 1938, as amended to treat certain tax-exempt organizations receiving funding from foreign principals of foreign countries of concern as agents of a foreign principal under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:18:28Z"
    }
  ]
}
```
