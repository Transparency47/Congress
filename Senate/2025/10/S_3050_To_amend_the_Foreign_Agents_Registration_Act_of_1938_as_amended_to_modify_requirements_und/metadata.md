# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3050?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3050
- Title: PAID OFF Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3050
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2026-04-16T20:31:15Z
- Update date including text: 2026-04-16T20:31:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3050",
    "number": "3050",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "PAID OFF Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T20:31:15Z",
    "updateDateIncludingText": "2026-04-16T20:31:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
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
      "actionDate": "2025-10-23",
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
          "date": "2025-10-23T19:34:21Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "RI"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "ID"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "NE"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "TN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "NC"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "VT"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "IA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-10-23",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3050is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3050\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mr. Cornyn (for himself, Mr. Whitehouse , Mr. Risch , Mrs. Fischer , Mr. Hagerty , Mr. Tillis , Mr. Welch , Mr. Grassley , and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Foreign Agents Registration Act of 1938, as amended, to modify requirements under that Act relating to exemptions, and for other purposes.\n#### 1. Treatment of exemptions under the Foreign Agents Registration Act of 1938\nThis Act may be cited as the Preventing Adversary Influence, Disinformation, and Obscured Foreign Financing Act of 2025 or the PAID OFF Act of 2025 .\n#### 2. Treatment of exemptions under the Foreign Agents Registration Act of 1938\nSection 3 of the Foreign Agents Registration Act of 1938, as amended ( 22 U.S.C. 613 ), is amended\u2014\n**(1)**\nin the matter preceding subsection (a), by inserting , except as provided in subsection (i) after principals ; and\n**(2)**\nby adding at the end the following:\n(i) Limitations The exemptions under subsections (d)(1), (d)(2), and (h) shall not apply to any agent of a foreign principal that is a corporate or government entity that is owned or controlled by 1 or more of the identified countries listed in clauses (i) through (v) of section 1(m)(1)(A) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m)(1)(A) ). .\n#### 3. Mechanism to amend definition of country of concern\nSection 1(m) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (6) and (7) as paragraphs (7) and (8), respectively; and\n**(2)**\nby inserting after paragraph (5) the following:\n(6) Modification to definition of country of concern (A) In general The Secretary of State may, in consultation with the Attorney General, propose the addition or deletion of countries described in paragraph (1)(A). (B) Submission Any proposal described in subparagraph (A) shall\u2014 (i) be submitted to the Chairman and Ranking Member of the Committee on Foreign Relations of the Senate and the Chairman and Ranking Member of the Committee on the Judiciary of the House of Representatives; and (ii) become effective upon enactment of a joint resolution of approval as described in subparagraph (C). (C) Joint resolution of approval (i) In general For purposes of subparagraph (B)(ii), the term joint resolution of approval means only a joint resolution\u2014 (I) that does not have a preamble; (II) that includes in the matter after the resolving clause the following: That Congress approves the modification of the definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956, as submitted by the Secretary of State on ____; and section 1(m)(1)(A) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(m)(1)(A) ) is amended by ______. , the blank spaces being appropriately filled in with the appropriate date and the amendatory language required to modify the list of countries in paragraph (1)(A) of this subsection by adding or deleting 1 or more countries; and (III) the title of which is as follows: Joint resolution approving modifications to definition of country of concern under section 1(m) of the State Department Basic Authorities Act of 1956. . (ii) Referral (I) Senate A resolution described in clause (i) that is introduced in the Senate shall be referred to the Committee on Foreign Relations of the Senate. (II) House of Representatives A resolution described in clause (i) that is introduced in the House of Representatives shall be referred to the Committee on the Judiciary of the House of Representatives. .\n#### 4. Sunset\nThe amendments made by this Act shall terminate on the date that is 5 years after the date of enactment of this Act.",
      "versionDate": "2025-10-23",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-18",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on the Judiciary, and Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6107",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PAID OFF Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-11-20T17:23:35Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3050is.xml"
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
      "title": "PAID OFF Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PAID OFF Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Adversary Influence, Disinformation, and Obscured Foreign Financing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Foreign Agents Registration Act of 1938, as amended, to modify requirements under that Act relating to exemptions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T03:48:12Z"
    }
  ]
}
```
