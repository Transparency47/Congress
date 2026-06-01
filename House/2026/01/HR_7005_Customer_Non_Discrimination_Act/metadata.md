# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7005?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7005
- Title: Customer Non-Discrimination Act
- Congress: 119
- Bill type: HR
- Bill number: 7005
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-04-29T17:05:07Z
- Update date including text: 2026-04-29T17:05:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7005",
    "number": "7005",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Customer Non-Discrimination Act",
    "type": "HR",
    "updateDate": "2026-04-29T17:05:07Z",
    "updateDateIncludingText": "2026-04-29T17:05:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
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
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
          "date": "2026-01-09T14:01:10Z",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "WI"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "DC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "IN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "WA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "LA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "GA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7005ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7005\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mrs. Watson Coleman (for herself, Mr. Tonko , Mr. Pocan , Ms. Crockett , Ms. Norton , Mr. Peters , Ms. Tlaib , Mr. Mullin , Mr. Johnson of Georgia , Mr. Carson , Mr. Thanedar , Mr. Takano , Ms. Garcia of Texas , Ms. Schakowsky , Ms. Jayapal , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit discrimination in public accommodations on the basis of sex, gender identity, and sexual orientation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Customer Non-Discrimination Act .\n#### 2. Public accommodations\n##### (a) Prohibition on discrimination or segregation in public accommodations\nSection 201 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a ) is amended\u2014\n**(1)**\nin subsection (a), by inserting sex (including sexual orientation and gender identity), before or national origin ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by striking stadium and all that follows and inserting stadium or other place of or establishment that provides exhibition, entertainment, recreation, exercise, amusement, gathering, or display; ;\n**(B)**\nby redesignating paragraph (4) as paragraph (6); and\n**(C)**\nby inserting after paragraph (3) the following:\n(4) any establishment that provides a good, service, or program, including a store, shopping center, online retailer or service provider, salon, bank, gas station, food bank, service or care center, shelter, travel agency, or funeral parlor, or establishment that provides health care, accounting, or legal services; (5) any train service, bus service, car service, taxi service, airline service, station, depot, or other place of or establishment that provides transportation service; and .\n##### (b) Prohibition on discrimination or segregation under law\nSection 202 of such Act ( 42 U.S.C. 2000a\u20131 ) is amended by inserting sex (including sexual orientation and gender identity), before or national origin .\n##### (c) Definitions and rules of construction\nTitle II of such Act ( 42 U.S.C. 2000a et seq. ) is amended by adding at the end the following:\n208. Definitions and rules (a) Definitions (1) Race; color; religion; sex; sexual orientation; gender identity; national origin The term race , color , religion , sex (including sexual orientation and gender identity) , or national origin , used with respect to an individual, includes\u2014 (A) the race, color, religion, sex (including sexual orientation and gender identity), or national origin, respectively, of another person with whom the individual is associated or has been associated; and (B) a perception or belief, even if inaccurate, concerning the race, color, religion, sex (including sexual orientation and gender identity), or national origin, respectively, of the individual. (2) Gender identity The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth. (3) Including The term including means including, but not limited to, consistent with the term\u2019s standard meaning in Federal law. (4) Sex The term sex includes\u2014 (A) a sex stereotype; (B) pregnancy, childbirth, or a related medical condition; (C) sexual orientation or gender identity; and (D) sex characteristics, including intersex traits. (5) Sexual orientation The term sexual orientation means homosexuality, heterosexuality, or bisexuality. (b) Rules In this title\u2014 (1) (with respect to sex) pregnancy, childbirth, or a related medical condition shall not receive less favorable treatment than other physical conditions; and (2) (with respect to gender identity) an individual shall not be denied access to a shared facility, including a restroom, a locker room, and a dressing room, that is in accordance with the individual\u2019s gender identity. 209. Rules of construction (a) Claims and remedies not precluded Nothing in this title shall be construed to limit the claims or remedies available to any individual for an unlawful practice on the basis of race, color, religion, sex (including sexual orientation and gender identity), or national origin including claims brought pursuant to section 1979 or 1980 of the Revised Statutes ( 42 U.S.C. 1983 , 1985) or any other law, including the Federal law amended by the Customer Non-Discrimination Act, regulation, or policy. (b) No negative inference Nothing in this title shall be construed to support any inference that any Federal law prohibiting a practice on the basis of sex does not prohibit discrimination on the basis of pregnancy, childbirth, or a related medical condition, sexual orientation, gender identity, or a sex stereotype. (c) Scope of an establishment A reference in this title to an establishment\u2014 (1) shall be construed to include an individual whose operations affect commerce and who is a provider of a good, service, or program; and (2) shall not be construed to be limited to a physical facility or place. 210. Claims The Religious Freedom Restoration Act of 1993 ( 42 U.S.C. 2000bb et seq. ) shall not provide a claim concerning, or a defense to a claim under this title or provide a basis for challenging the application or enforcement of this title. .",
      "versionDate": "2026-01-09",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1354",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Justice for All Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-29",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1503",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equality Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-29",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Education and Workforce, Financial Services, House Administration, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "15",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equality Act",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-01-26T14:47:10Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7005ih.xml"
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
      "title": "Customer Non-Discrimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Customer Non-Discrimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit discrimination in public accommodations on the basis of sex, gender identity, and sexual orientation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:49Z"
    }
  ]
}
```
