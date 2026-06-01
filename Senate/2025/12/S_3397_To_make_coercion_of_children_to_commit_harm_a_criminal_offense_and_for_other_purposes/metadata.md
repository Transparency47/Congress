# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3397?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3397
- Title: ECCHO Act
- Congress: 119
- Bill type: S
- Bill number: 3397
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3397",
    "number": "3397",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "ECCHO Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
            "date": "2025-12-09T19:40:25Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-09T19:40:25Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "SC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-02",
      "state": "ME"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "AZ"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "GA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3397is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3397\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Grassley (for himself, Mr. Durbin , Ms. Klobuchar , Mr. Cornyn , and Mr. Graham ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo make coercion of children to commit harm a criminal offense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ending Coercion of Children and Harm Online or the ECCHO Act .\n#### 2. Coercion of children to commit harm\nChapter 110A of title 18, United States Code, is amended by inserting after section 2261B the following:\n2261C. Coercion of children to commit harm (a) Definitions For purposes of this section: (1) Coerce The term coerce includes the use of extortion, threats, fraud, deceit, duress, intimidation, harassment, humiliation, degradation, or manipulation. (2) Covered act The term covered act means doxxing, swatting, or making a false report about an active or imminent threat. (3) Doxxing The term doxxing means the act of publishing the personally identifiable information of an individual for the purpose of harassing or intimidating the individual. (4) Minor The term minor means any individual who has not attained the age of 18 years. (5) Substantial bodily injury The term substantial bodily injury has the meaning given that term in section 113. (6) Swatting The term swatting means the act of making a false report to emergency services about an individual for the purpose of causing a special weapons and tactics team to respond to the location of the individual. (b) Offense It shall be unlawful for any person, using the mail or any facility or means of interstate or foreign commerce, or within the special maritime and territorial jurisdiction of the United States, to intentionally coerce a minor, directly or through an intermediary, to\u2014 (1) (A) die by suicide or attempt to die by suicide; or (B) kill or attempt to kill any individual; (2) kill or attempt to kill any, pet, emotional support animal, service animal, or horse; (3) strangle, suffocate, poison, burn, lacerate, or inflict serious bodily injury or substantial bodily injury on any individual (including the minor), pet, emotional support animal, service animal, or horse; or (4) commit, or attempt to commit\u2014 (A) arson; or (B) a covered act for which any person can be charged with a criminal offense. (c) Penalty Any person who violates, or attempts or conspires to violate\u2014 (1) subparagraph (A) or (B) of subsection (b)(1) shall be fined under this title, imprisoned for any term of years or life, or both; or (2) paragraph (2), (3), or (4) of subsection (b) shall be fined under this title, imprisoned not more than 30 years, or both. .\n#### 3. Clerical and conforming amendments\n##### (a) Clerical amendment\nThe table of sections for chapter 110A of title 18, United States Code, is amended by inserting after the item relating to section 2261B the following:\n2261C. Coercion of children to commit harm .\n##### (b) Conforming amendments\n**(1) Title 18**\n**(A) Chapter 110**\nChapter 110 of title 18, United States Code, is amended\u2014\n**(i)**\nin section 2252A(g), by inserting section 2261C, after section 1591, ; and\n**(ii)**\nin section 2258A\u2014\n**(I)**\nin subsection (a)\u2014\n**(aa)**\nin paragraph (1)(A), by striking online child sexual exploitation and to prevent the online sexual exploitation of children and inserting , and to prevent, online child sexual exploitation and online coercion of children ; and\n**(bb)**\nin paragraph (2)(A)\u2014\n(AA)\nby striking or 2260 that involves child pornography, and inserting 2260, 2261C, or 2422(b), or ; and\n(BB)\nby striking , or of 2422(b) ;\n**(II)**\nin subsection (b), in the matter preceding paragraph (1), by striking sexual and inserting online ;\n**(III)**\nin subsection (c)\u2014\n**(aa)**\nin paragraph (1), by striking , kidnapping or enticement crimes and inserting or kidnapping, online coercion, or enticement crimes involving children ;\n**(bb)**\nin paragraph (2), by inserting or kidnapping, online coercion, or enticement crimes involving children after sexual exploitation ; and\n**(cc)**\nin paragraph (3), by striking , kidnapping or enticement crimes and inserting or kidnapping, online coercion, or enticement crimes involving children ;\n**(IV)**\nin subsection (d)(5)(A)(ii)(II), by striking , kidnapping, or enticement crimes and inserting or kidnapping, online coercion, or enticement crimes involving children ;\n**(V)**\nin subsection (g)(3)\u2014\n**(aa)**\nin subparagraph (A), by striking , kidnapping, or enticement crimes and inserting or kidnapping, online coercion, or enticement crimes involving children ;\n**(bb)**\nin subparagraph (B), by striking , kidnapping, or enticement crimes and inserting or kidnapping, online coercion, or enticement crimes involving children ; and\n**(cc)**\nin subparagraph (C), by striking , kidnapping, or enticement crimes and inserting or kidnapping, online coercion, or enticement crimes involving children ; and\n**(VI)**\nin subsection (h)(5), by striking the proliferation of online child sexual exploitation or preventing the online sexual exploitation of children and inserting or preventing the proliferation of online child sexual exploitation or online coercion of children .\n**(B) Section 3509**\nSection 3509(a)(2)(A) of title 18, United States Code, is amended by striking physical abuse, sexual abuse, or exploitation and inserting child abuse .\n**(C) Section 5032**\nSection 5032 of title 18, United States Code\u2014\n**(i)**\nin the first undesignated paragraph\u2014\n**(I)**\nby striking or section 1002(a) and inserting section 1002(a) ; and\n**(II)**\nby striking section 922(x) or section 924(b), (g), or (h) of this title and inserting or section 922(x), section 924(b), (g), or (h), or section 2261C of this title ; and\n**(ii)**\nin the fourth undesignated paragraph, by striking section 922(x) of this title, or in section 924(b), (g), or (h) of this title and inserting section 922(x), section 924(b), (g), or (h), or section 2261C of this title .\n**(2) PROTECT Our Children Act of 2008**\nSection 2 of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21101 ) is amended by striking paragraph (1) and inserting the following:\n(1) Child exploitation The term child exploitation means\u2014 (A) any conduct, attempted conduct, or conspiracy to engage in conduct that\u2014 (i) violates chapter 110 or section 2261C, 2422(b), or 2423 of title 18; or (ii) involves a minor and violates section 1591 or chapter 109A of title 18; or (B) any sexual activity involving a minor for which any person can be charged with a criminal offense. .\n#### 4. Severability\nIf any provision of this Act, an amendment made by this Act, or the application of such a provision or amendment to any person or circumstance, is held to be unconstitutional, the remaining provisions of and amendments made by this Act, and the application of the provision or amendment held to be unconstitutional to any other person or circumstance, shall not be affected thereby.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2026-03-02",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 346."
      },
      "number": "6719",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "James T. Woods Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-07T16:57:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
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
          "measure-id": "id119s3397",
          "measure-number": "3397",
          "measure-type": "s",
          "orig-publish-date": "2025-12-09",
          "originChamber": "SENATE",
          "update-date": "2026-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3397v00",
            "update-date": "2026-02-27"
          },
          "action-date": "2025-12-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ending Coercion of Children and Harm Online or the ECCHO Act</strong></p><p>This bill establishes a federal framework to combat the online coercion of minors to commit harm. The bill\u00a0creates new criminal offenses, expands reporting of instances involving the online coercion of minors, facilitates the prosecution of offenders, and expands protections for minors who testify in court.</p><p>Specifically, the bill makes it a crime to intentionally coerce a minor to</p><ul><li>commit suicide (or attempt to);</li><li>kill someone (or attempt to);</li><li>kill a pet, emotional support animal, service animal, or horse (or attempt to);</li><li>physically harm an individual (including the minor), pet, emotional support animal, service animal, or horse; or</li><li>commit (or attempt to commit) arson or certain other acts such as doxxing or swatting.</li></ul><p>A violation (or conspiracy or attempt to commit a violation) is subject to a fine, a prison term, or both.</p><p>The bill requires electronic communication service providers and remote computing service providers to report instances of online coercion of minors to the National Center for Missing & Exploited Children\u00a0via the CyberTipline.</p><p>The bill facilitates the federal prosecution of offenses committed by (1) individuals as part of a child exploitation enterprise, and (2) minors in certain circumstances.</p><p>The bill extends various protections for minors who testify in court (e.g., certain privacy protections) to those who are victims of or witnesses to crimes involving mental injury (i.e., psychological or intellectual harm to a child) or the negligent treatment of a child.</p>"
        },
        "title": "ECCHO Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3397.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ending Coercion of Children and Harm Online or the ECCHO Act</strong></p><p>This bill establishes a federal framework to combat the online coercion of minors to commit harm. The bill\u00a0creates new criminal offenses, expands reporting of instances involving the online coercion of minors, facilitates the prosecution of offenders, and expands protections for minors who testify in court.</p><p>Specifically, the bill makes it a crime to intentionally coerce a minor to</p><ul><li>commit suicide (or attempt to);</li><li>kill someone (or attempt to);</li><li>kill a pet, emotional support animal, service animal, or horse (or attempt to);</li><li>physically harm an individual (including the minor), pet, emotional support animal, service animal, or horse; or</li><li>commit (or attempt to commit) arson or certain other acts such as doxxing or swatting.</li></ul><p>A violation (or conspiracy or attempt to commit a violation) is subject to a fine, a prison term, or both.</p><p>The bill requires electronic communication service providers and remote computing service providers to report instances of online coercion of minors to the National Center for Missing & Exploited Children\u00a0via the CyberTipline.</p><p>The bill facilitates the federal prosecution of offenses committed by (1) individuals as part of a child exploitation enterprise, and (2) minors in certain circumstances.</p><p>The bill extends various protections for minors who testify in court (e.g., certain privacy protections) to those who are victims of or witnesses to crimes involving mental injury (i.e., psychological or intellectual harm to a child) or the negligent treatment of a child.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s3397"
    },
    "title": "ECCHO Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ending Coercion of Children and Harm Online or the ECCHO Act</strong></p><p>This bill establishes a federal framework to combat the online coercion of minors to commit harm. The bill\u00a0creates new criminal offenses, expands reporting of instances involving the online coercion of minors, facilitates the prosecution of offenders, and expands protections for minors who testify in court.</p><p>Specifically, the bill makes it a crime to intentionally coerce a minor to</p><ul><li>commit suicide (or attempt to);</li><li>kill someone (or attempt to);</li><li>kill a pet, emotional support animal, service animal, or horse (or attempt to);</li><li>physically harm an individual (including the minor), pet, emotional support animal, service animal, or horse; or</li><li>commit (or attempt to commit) arson or certain other acts such as doxxing or swatting.</li></ul><p>A violation (or conspiracy or attempt to commit a violation) is subject to a fine, a prison term, or both.</p><p>The bill requires electronic communication service providers and remote computing service providers to report instances of online coercion of minors to the National Center for Missing & Exploited Children\u00a0via the CyberTipline.</p><p>The bill facilitates the federal prosecution of offenses committed by (1) individuals as part of a child exploitation enterprise, and (2) minors in certain circumstances.</p><p>The bill extends various protections for minors who testify in court (e.g., certain privacy protections) to those who are victims of or witnesses to crimes involving mental injury (i.e., psychological or intellectual harm to a child) or the negligent treatment of a child.</p>",
      "updateDate": "2026-02-27",
      "versionCode": "id119s3397"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3397is.xml"
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
      "title": "ECCHO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ECCHO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ending Coercion of Children and Harm Online",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to make coercion of children to commit harm a criminal offense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:23Z"
    }
  ]
}
```
