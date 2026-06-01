# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4192?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4192
- Title: PLOT Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4192
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-09T17:20:21Z
- Update date including text: 2026-04-09T17:20:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4192",
    "number": "4192",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "PLOT Act of 2026",
    "type": "S",
    "updateDate": "2026-04-09T17:20:21Z",
    "updateDateIncludingText": "2026-04-09T17:20:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T17:19:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4192is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4192\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Ricketts introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Foreign Investment Disclosure Act of 1978 to require reports to contain geospatial data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Property Location Oversight and Transparency Act of 2026 or the PLOT Act of 2026 .\n#### 2. Geospatial data requirements\nSection 2 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 ) is amended by adding at the end the following:\n(g) Geospatial data collection (1) In general Any person that submits a report under this section shall include in the report geospatial data delineating the property boundaries of the applicable agricultural land. (2) Format The geospatial data required under paragraph (1) shall be submitted in an open-source format compatible with widely available geographic information system software, such as a quantum geographic information system or equivalent format, approved by the Secretary. (3) Accessibility (A) In general The Secretary may make geospatial data submitted in reports under this section available to Federal, State, and local agencies and the public for purposes of oversight, transparency, and national security. (B) National security applications The Secretary, in consultation with the Director of National Intelligence and the Secretary of Defense, shall use geospatial data submitted in reports under this section to identify potential national security concerns relating to foreign ownership of agricultural land, including proximity to military installations, critical infrastructure, and sensitive environmental areas. .\n#### 3. Foreign adversaries\nNot later than 180 days after the date of enactment of this Act, the Secretary of Agriculture shall revise section 781.2 of title 7, Code of Federal Regulations, to require that\u2014\n**(1)**\nin the case of a person that submits a report under section 2 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 ) relating to a transaction involving a person associated with a foreign adversary (as defined in section 9 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3508 ))\u2014\n**(A)**\nthe percentage under subsection (k)(1) shall be 5 percent;\n**(B)**\nthe percentage under subsection (k)(2) shall be 10 percent; and\n**(C)**\nthe percentage under subsection (k)(3) shall be 20 percent; and\n**(2)**\nany person that submits a report under section 2 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 ) shall disclose any foreign adversary (as so defined), or any person affiliated with a foreign adversary, that holds an interest in that person that is 5 percent or greater.\n#### 4. Investigative actions\nSection 4 of the Agricultural Foreign Investment Disclosure Act of ( 7 U.S.C. 3503 ) is amended\u2014\n**(1)**\nby striking the section designation and all that follows through The Secretary and inserting the following:\n4. Investigative actions (a) In general The Secretary ; and\n**(2)**\nby adding at the end the following:\n(b) Enforcement prioritization The Secretary shall prioritize enforcement actions, including investigations, audits, compliance reviews, and penalties, for transactions involving foreign adversaries, with priority given to persons associated with the People's Republic of China. (c) Referrals to CFIUS The Secretary shall refer to the Committee on Foreign Investment in the United States any transaction that the Secretary determines may pose a national security risk. .\n#### 5. Definition of foreign adversary\nSection 9 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3508 ) is amended\u2014\n**(1)**\nby striking the section designation and all that follows through this Act\u2014 in the matter preceding paragraph (1) and inserting the following:\n9. Definitions In this Act: ;\n**(2)**\nin each of paragraphs (1) through (6)\u2014\n**(A)**\nby striking the term and inserting The term ; and\n**(B)**\nby inserting a paragraph heading, the text of which comprises the term defined in that paragraph;\n**(3)**\nin each of paragraphs (1) through (4), by striking the semicolon at the end of the paragraph and inserting a period;\n**(4)**\nin paragraph (5), by striking ; and and inserting a period;\n**(5)**\nby redesignating paragraphs (2) through (6) as paragraphs (3) through (7), respectively; and\n**(6)**\nby inserting after paragraph (1) the following:\n(2) Foreign adversary The term foreign adversary has the meaning given the term in section 791.2 of title 15, Code of Federal Regulations (or a successor regulation), including the entities described in section 791.4 of that title (or a successor regulation). .\n#### 6. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-03-25",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-09T17:20:21Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4192is.xml"
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
      "title": "PLOT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PLOT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Property Location Oversight and Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Foreign Investment Disclosure Act of 1978 to require reports to contain geospatial data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:33Z"
    }
  ]
}
```
