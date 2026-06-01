# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1600?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1600
- Title: Save Healthcare Workers Act
- Congress: 119
- Bill type: S
- Bill number: 1600
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1600",
    "number": "1600",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Save Healthcare Workers Act",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T22:29:03Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-05",
      "state": "ME"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "ID"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1600is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1600\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mrs. Hyde-Smith (for herself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo protect hospital personnel from violence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save Healthcare Workers Act .\n#### 2. Prevention of violence against hospital personnel\n##### (a) Prohibition on assault of hospital personnel in the performance of duties\nChapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Assault of hospital personnel (a) In general Whoever knowingly assaults an individual employed by a hospital engaged in interstate commerce, or an entity contracting with a hospital or other medical facility engaged in interstate commerce, on the grounds of a hospital while the individual is engaged in or on account of duties at the hospital shall be fined under this title, imprisoned for not more than 10 years, or both. (b) Enhanced penalties (1) Acts involving dangerous weapons or acts that result in bodily injury Whoever, in the commission of any act described in subsection (a), uses a firearm or dangerous weapon or inflicts serious bodily injury, shall, in addition to the penalties provided for in that subsection, be fined under this title, imprisoned for not more than 20 years, or both. (2) Acts committed during emergency declarations Whoever commits any act described in subsection (a) during the period of a declaration of a public emergency for the area in which the act is committed shall be fined under this title, imprisoned for not more than 20 years, or both. (c) Affirmative defense (1) In general It shall be an affirmative defense to a prosecution under this section that\u2014 (A) the defendant is a person with a physical, mental, or intellectual disability; (B) the conduct of the defendant was a clear and direct manifestation of such disability; and (C) the defendant, as a result of such disability, was unable to appreciate the nature and quality or wrongfulness of such conduct. (2) Burden of proof The defendant has the burden of proving the defense under this subsection by a preponderance of the evidence. (d) Definitions In this section: (1) Dangerous weapon The term dangerous weapon means a weapon, device, instrument, material, or substance, animate or inanimate, that is used for, or is readily capable of, causing death or serious bodily injury. (2) Declaration of a public emergency The term declaration of a public emergency means an emergency or major disaster declared by the President pursuant to the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ). (3) Disability The term disability means a disability described in section 3(1)(A) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102(1)(A) ). (4) Grounds of a hospital The term grounds of a hospital means the hospital buildings and the land used for the purposes of the hospital, including all buildings, roads, paths, and open spaces. (5) Hospital The term hospital means any of the following medical facilities: (A) A hospital (as defined in section 1861(e) of the Social Security Act ( 42 U.S.C. 1395x(e) )). (B) A long-term care hospital (as defined in section 1861(ccc) of such Act ( 42 U.S.C. 1395x(ccc) )). (C) A rehabilitation facility (as described in section 1886(j)(1)(A) of such Act ( 42 U.S.C. 1395ww(j)(1)(A) )). (D) A children's hospital (as described in section 1886(d)(1)(B)(iii) of such Act ( 42 U.S.C. 1395ww(d)(1)(B)(iii) )). (E) A cancer hospital (as described in section 1886(d)(1)(B)(v) of such Act ( 42 U.S.C. 1395ww(d)(1)(B)(v) )). (F) A critical access hospital (as defined in section 1861(mm)(1) of such Act ( 42 U.S.C. 1395x(mm)(1) )). (G) A rural emergency hospital (as defined in section 1861(kkk)(2) of such Act ( 42 U.S.C. 1395x(kkk)(2) )). (6) Serious bodily injury The term serious bodily injury has the meaning given the term in section as the meaning given the term in section 1365(h). .\n##### (b) Clerical amendment\nThe table of sections for chapter 7 of title 18, United States Code, is amended by adding at the end the following:\n120. Assault of hospital personnel. .\n#### 3. GAO study\nThe Comptroller General of the United States shall conduct a study on\u2014\n**(1)**\nhow this Act, and the amendments made by this Act, has affected workplace violence in healthcare settings; and\n**(2)**\nwhether Federal, State, Tribal, and local prosecutions for workplace violence in healthcare settings have increased or decreased because of the ability to prosecute these incidents as Federal crimes.",
      "versionDate": "2025-05-05",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-22T17:30:09Z"
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
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1600is.xml"
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
      "title": "Save Healthcare Workers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-16T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Save Healthcare Workers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect hospital personnel from violence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:20Z"
    }
  ]
}
```
