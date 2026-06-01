# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1010
- Title: CAMPUS Act
- Congress: 119
- Bill type: S
- Bill number: 1010
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-07-30T12:48:19Z
- Update date including text: 2025-07-30T12:48:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1010",
    "number": "1010",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "CAMPUS Act",
    "type": "S",
    "updateDate": "2025-07-30T12:48:19Z",
    "updateDateIncludingText": "2025-07-30T12:48:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
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
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T22:36:07Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TN"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1010is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1010\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Lankford introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit the use of funds for universities that provide support to the People\u2019s Liberation Army, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Countering Adversarial and Malicious Partnerships at Universities and Schools Act of 2025 or the CAMPUS Act .\n#### 2. Identification of entities engaged in Military-Civil Fusion in the People's Republic of China\n##### (a) In general\nThe Director of National Intelligence, in consultation with the Secretary of Defense, shall identify each institution of higher education domiciled in the People\u2019s Republic of China that provides support to the People\u2019s Liberation Army, including any such institution involved in the implementation of the Military-Civil Fusion strategy of the People\u2019s Republic of China or that participates in the defense industrial base of the People\u2019s Republic of China.\n##### (b) Submission of list to Congress\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Director of National Intelligence shall submit to the appropriate committees of Congress a list of each entity identified under subsection (a).\n#### 3. Prohibition on use of funds for entities engaged in Military-Civil Fusion\nNone of the funds authorized to be appropriated or otherwise made available for the Department of Defense for research, development, testing, and evaluation may be provided to an entity that maintains a contract with an institution identified under section 2.\n#### 4. Limitation on eligibility of facilities to host or store classified information\nThe Director of the Defense Counterintelligence and Security Agency may not determine that a facility of an entity is eligible to host or store a classified information unless the entity certifies to the Director that the entity does not have an active research partnership with an institution that is included in the list submitted under section 2(b).\n#### 5. Denial of visas to individuals involved in Military-Civil Fusion\nThe Secretary of State may deny the application for a visa for a nonimmigrant described in subparagraph (F) or (J) of section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ) who is a student or employee of an institution identified under section 2.\n#### 6. Limitation on uses of funds for K-12 education\nNone of the funds authorized to be appropriated or otherwise made available to the Department of Education for K\u201312 education by may be provided to an elementary of secondary school that maintains a contract with an entity domiciled in the People\u2019s Republic of China.\n#### 7. Partnership with Taiwan\n##### (a) Sense of Congress\nIt is the sense of Congress that the American Institute in Taiwan should take steps to strengthen and expand partnerships with the Taipei Economic and Cultural Representatives Office in the United States to expand access to Mandarin language instruction and Chinese cultural programming for students in the United States, including K\u201312 schools and institutions of higher education.\n##### (b) Grant authority\nThe Secretary of Education is authorized to provide grants to K\u201312 schools and institutions of higher education to support access to Mandarin language instruction and Chinese cultural programming in the United States provided in partnership between the American Institute in Taiwan and Taipei Economic and Cultural Representatives Office in the United States, including programming under the United States-Taiwan Education Initiative.\n#### 8. Prohibition on use of funds for Federal grants with entities on the Entity List\nNone of the funds authorized to be appropriated or otherwise made available for research, development, testing, and evaluation may be provided to an entity that maintains a contract with an entity domiciled in the People\u2019s Republic of China that is identified on the list required under section 2(b) or listed on the Entity List maintained by the Bureau of Industry and Security at the Department of Commerce and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations.\n#### 9. Disclosure of foreign gifts\nSection 117(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1011f(a) ) is amended by striking $250,000 and inserting $50,000 .\n#### 10. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Armed Services, the Select Committee on Intelligence, and the Committee on Health, Education, Labor, and Pensions of the Senate; and\n**(B)**\nthe Committee on Armed Services, the Permanent Select Committee on Intelligence, and the Committee on Education and the Workforce of the House of Representatives.\n**(2) Institution of higher education**\nThe term institution of higher education domiciled in the People\u2019s Republic of China means an institution under the control or supervision, in whole or in part, of\u2014\n**(A)**\nthe Ministry of Education of the People\u2019s Republic of China; or\n**(B)**\nthe State Administration of Science, Technology, and Industry for National Defense of the People\u2019s Republic of China.\n**(3) K\u201312 schools**\nThe term K\u201312 education has the meaning given the term in section 5002(10) of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401(10) ).",
      "versionDate": "2025-03-12",
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
        "name": "International Affairs",
        "updateDate": "2025-05-20T18:22:06Z"
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
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1010is.xml"
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
      "title": "CAMPUS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CAMPUS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Countering Adversarial and Malicious Partnerships at Universities and Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of funds for universities that provide support to the People's Liberation Army, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:20Z"
    }
  ]
}
```
