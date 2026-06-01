# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2547?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2547
- Title: Kate's Law
- Congress: 119
- Bill type: S
- Bill number: 2547
- Origin chamber: Senate
- Introduced date: 2025-07-30
- Update date: 2026-03-10T11:03:22Z
- Update date including text: 2026-03-10T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-30: Introduced in Senate
- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-30: Introduced in Senate

## Actions

- 2025-07-30 - IntroReferral: Introduced in Senate
- 2025-07-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-30",
    "latestAction": {
      "actionDate": "2025-07-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2547",
    "number": "2547",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Kate's Law",
    "type": "S",
    "updateDate": "2026-03-10T11:03:22Z",
    "updateDateIncludingText": "2026-03-10T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-30",
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
            "date": "2025-07-30T20:13:37Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-30T20:13:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "NC"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "WV"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "NE"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2547is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2547\nIN THE SENATE OF THE UNITED STATES\nJuly 30, 2025 Mr. Cruz (for himself, Mr. Budd , Mr. Justice , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to increase penalties for individuals who illegally enter and reenter the United States after being removed, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kate's Law .\n#### 2. Commission of crimes by aliens who are unlawfully present in the United States\nSection 275 of the Immigration and Nationality Act ( 8 U.S.C. 1325 ) is amended\u2014\n**(1)**\nin subsection (a), by striking 2 years and inserting 5 years ; and\n**(2)**\nby adding at the end the following:\n(e) Any alien who\u2014 (1) (A) enters or attempts to enter the United States at any time or place other than as designated by immigration officers; (B) eludes examination or inspection by immigration officers; or (C) attempts to enter or obtains entry to the United States by a willfully false or misleading representation or the willful concealment of a material fact, and (2) thereafter is convicted of any crime punishable by more than 1 year of imprisonment, may be fined under title 18, United States Code, and shall be imprisoned for a term of not less than 5 years. .\n#### 3. Increased penalties for reentry of removed alien\nSection 276 of the Immigration and Nationality Act ( 8 U.S.C. 1326 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) and (d) as subsections (e) and (f), respectively;\n**(2)**\nby striking subsections (a) and (b) and inserting the following:\n(a) In general Except as provided in subsections (b), (c), and (d), any alien who\u2014 (1) has been denied admission, excluded, deported, removed, or has departed the United States while an order of exclusion, deportation, or removal is outstanding; and (2) thereafter enters, attempts to enter, or is at any time found in, the United States\u2014 shall be fined under title 18, United States Code, imprisoned not more than 10 years, or both. (b) Exceptions An alien shall not be subject to the penalty under subsection (a) if\u2014 (1) the Secretary of Homeland Security has expressly consented to such alien\u2019s reapplying for admission before the alien\u2019s reembarkation at a place outside the United States or the alien\u2019s application for admission from foreign contiguous territory; or (2) an alien previously denied admission and removed establishes that he or she alien was not required to obtain such advance consent under this Act. (c) Criminal penalties for reentry of certain removed aliens (1) In general Notwithstanding subsection (a), and except as provided in subsection (d)\u2014 (A) an alien described in subsection (a) who was convicted before such removal or departure of 3 or more misdemeanors involving drugs, crimes against the person, or both shall be fined under title 18, United States Code, imprisoned not more than 15 years, or both; (B) an alien described in subsection (a) who has been excluded from the United States pursuant to section 235(c) because the alien was inadmissible under section 212(a)(3)(B) or who has been removed from the United States pursuant to the provisions of title V, and who thereafter, without the permission of the Secretary of Homeland Security, enters the United States, or attempts to do so, shall be fined under title 18, United States Code, and imprisoned for a period of 10 years, which sentence shall not run concurrently with any other sentence; (C) an alien described in subsection (a) who was removed from the United States pursuant to section 241(a)(4)(B) who thereafter, without the permission of the Secretary of Homeland Security, enters, attempts to enter, or is at any time found in, the United States, shall be fined under title 18, United States Code, imprisoned for not more than 10 years, or both; and (D) an alien described in subsection (a) who has been denied admission, excluded, deported, or removed 3 or more times and thereafter enters, attempts to enter, or is at any time found in the United States, shall be fined under title 18, United States Code, imprisoned not more than 10 years, or both. (2) Removal defined In this subsection and in subsection (d), the term removal includes any agreement in which an alien stipulates to removal during (or not during) a criminal trial under either Federal or State law. (d) Mandatory minimum criminal penalty for reentry of certain removed aliens An alien described in subsection (a)\u2014 (1) who was convicted before such removal or departure of\u2014 (A) any aggravated felony; (B) any crime defined as a felony by the relevant jurisdiction (Federal, State, Tribal, or local) of conviction; or (C) any crime punishable by more than 1 year of imprisonment; or (2) who was convicted of a violation described in this section at least twice before such removal or departure, may be fined under title 18, United States Code, and shall be imprisoned for not less than 10 years. ; and\n**(3)**\nin subsection (e), as redesignated by paragraph (1)\u2014\n**(A)**\nby striking section 242(h)(2) and inserting section 241(a)(4) ; and\n**(B)**\nby striking Attorney General and inserting Secretary of Homeland Security .",
      "versionDate": "2025-07-30",
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
        "name": "Immigration",
        "updateDate": "2025-09-18T17:59:37Z"
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
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2547is.xml"
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
      "title": "Kate's Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Kate's Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to increase penalties for individuals who illegally enter and reenter the United States after being removed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:38Z"
    }
  ]
}
```
