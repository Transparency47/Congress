# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1543?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1543
- Title: EQUITY Act
- Congress: 119
- Bill type: HR
- Bill number: 1543
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2025-08-13T19:43:54Z
- Update date including text: 2025-08-13T19:43:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1543",
    "number": "1543",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "EQUITY Act",
    "type": "HR",
    "updateDate": "2025-08-13T19:43:54Z",
    "updateDateIncludingText": "2025-08-13T19:43:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NV"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "HI"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "VA"
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
      "sponsorshipDate": "2025-02-24",
      "state": "DC"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CA"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1543ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1543\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Ms. Strickland (for herself, Ms. Escobar , Ms. Sewell , Mr. Horsford , Ms. Tokuda , Ms. McClellan , Ms. Norton , Ms. Sherrill , Mr. Lieu , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to prohibit discrimination in the Armed Forces.\n#### 1. Short title\nThis Act may be cited as the Equal and Uniform Treatment in the Military Act or the EQUITY Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nWomen, Black, Native American, and LGBTQIA+ Americans have served in the Armed Forces since the Revolutionary War.\n**(2)**\nIn 1948, 16 years before the enactment of the Civil Rights Act ( Public Law 88\u2013352 ; 78 Stat. 241), which desegrated civilian spaces, President Truman issued Executive Order 9981, which allowed Black members of the Armed Forces to serve side-by-side with white members.\n**(3)**\nIn 1948, President Truman signed the Women\u2019s Armed Services Integration Act ( Public Law 80\u2013625 ; 62 Stat. 356) into law, officially allowing women to serve as full, permanent members of each Armed Force.\n**(4)**\nIn 1967, President Johnson signed into law Public Law 90\u2013130 , which authorized the promotion of women to the ranks of general and flag officers.\n**(5)**\nIn 1972, women were allowed to command units that included men.\n**(6)**\nIn 1982, the Department of Defense Instruction 1332.14, Enlisted Administrative Separations , banned homosexual individuals from serving in the Armed Forces.\n**(7)**\nIn 1993, President Clinton signed into law the National Defense Authorization Act for Fiscal Year 1994 ( Public Law 103\u201316 ), which enacted section 654 of title 10, United States Code, Policy concerning homosexuality in the armed forces , commonly known as Don\u2019t Ask, Don\u2019t Tell .\n**(8)**\nIn 2011, President Obama signed into law the Don\u2019t Ask, Don\u2019t Tell Repeal Act of 2010 , allowing homosexual members to openly serve in the Armed Forces.\n**(9)**\nIn 2015, the last remaining policy restrictions on women serving in direct combat roles were removed.\n**(10)**\nIn 2021, President Biden issued Executive Order 13988, which rescinded the policy that prohibited transgender individuals from serving in the Armed Forces.\n**(11)**\nIn 2025, President Trump issued Executive Order 14183, falsely stating that people who are transgender cannot satisfy the rigorous standards necessary for military service and that their identity conflicts with a soldier\u2019s commitment to an honorable, truthful, and disciplined lifestyle, even in one\u2019s personal life.\n**(12)**\nIt should be the policy of the United States that every member of the Armed Forces has the right to serve, advance, and be evaluated based on only individual merit, fitness, capability, and performance, in an environment free of discrimination on the basis of race, color, national origin, religion, sex, gender identity, or sexual orientation.\n#### 3. Nondiscrimination in the Armed Forces\nChapter 49 of title 10, United States Code, is amended by inserting after section 974 the following new section:\n975. Prohibition on discrimination (a) Prohibition (1) Subject to paragraph (2), discrimination within the Department of Defense against an individual on the basis of race, color, religion, sex, national origin, gender identity, or sexual orientation, is prohibited. (2) A qualification established or applied regarding eligibility for service in an armed force shall take into account only the ability of an individual to meet\u2014 (A) general occupational standards for military service; and (B) the particular military occupational specialty. (b) Definitions In this section: (1) The term gender identity means the gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth. (2) The term sex includes\u2014 (A) a sex stereotype; (B) pregnancy, childbirth, or a related medical condition; and (C) sex characteristics, including intersex traits. (3) The term sex stereotype includes\u2014 (A) stereotypical notions of masculinity or femininity; (B) an expectation of how an individual represents or communicates their gender to others through behavior, clothing, hairstyle, activity, voice, mannerism, or body characteristic; (C) the expectation that an individual will consistently identify with only one gender; and (D) an expectation regarding the appropriateness of a role for a certain sex. .",
      "versionDate": "2025-02-24",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-07-17T19:29:01Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-07-17T19:28:43Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-17T19:28:47Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2025-07-17T19:28:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T18:50:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1543",
          "measure-number": "1543",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-08-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1543v00",
            "update-date": "2025-08-13"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Equal and Uniform Treatment in the Military Act or the EQUITY Act\u00a0</strong></p><p>This bill prohibits discrimination within the Department of Defense (DOD) against individuals on the basis of race, color, religion, sex, national origin, gender identity, or sexual orientation.</p><p>A qualification established or applied related to eligibility for service in any of the Armed Forces\u00a0must only consider (1) the ability of an individual to meet the general occupational standards for service, and (2) the particular military occupational specialty.</p><p>On January 20, 2025, President Donald Trump signed an executive order titled <em>Defending Women from Gender Ideology Extremism and Restoring Biological Truth to the Federal Government</em>, declaring that the United States recognizes two sexes (male and female) and these sexes are not changeable.</p><p>On January 27, 2025, President Donald Trump signed an executive order titled<em> Prioritizing Military Excellence and Readiness</em>, expressing that the policy for troop readiness is inconsistent with gender dysphoria or the use of pronouns that inaccurately reflect an individual\u2019s biological sex. Further, the order directs DOD to update specific guidance documents related to medical standards for military service to reflect the purpose and policy of the order.</p>"
        },
        "title": "EQUITY Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1543.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Equal and Uniform Treatment in the Military Act or the EQUITY Act\u00a0</strong></p><p>This bill prohibits discrimination within the Department of Defense (DOD) against individuals on the basis of race, color, religion, sex, national origin, gender identity, or sexual orientation.</p><p>A qualification established or applied related to eligibility for service in any of the Armed Forces\u00a0must only consider (1) the ability of an individual to meet the general occupational standards for service, and (2) the particular military occupational specialty.</p><p>On January 20, 2025, President Donald Trump signed an executive order titled <em>Defending Women from Gender Ideology Extremism and Restoring Biological Truth to the Federal Government</em>, declaring that the United States recognizes two sexes (male and female) and these sexes are not changeable.</p><p>On January 27, 2025, President Donald Trump signed an executive order titled<em> Prioritizing Military Excellence and Readiness</em>, expressing that the policy for troop readiness is inconsistent with gender dysphoria or the use of pronouns that inaccurately reflect an individual\u2019s biological sex. Further, the order directs DOD to update specific guidance documents related to medical standards for military service to reflect the purpose and policy of the order.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119hr1543"
    },
    "title": "EQUITY Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Equal and Uniform Treatment in the Military Act or the EQUITY Act\u00a0</strong></p><p>This bill prohibits discrimination within the Department of Defense (DOD) against individuals on the basis of race, color, religion, sex, national origin, gender identity, or sexual orientation.</p><p>A qualification established or applied related to eligibility for service in any of the Armed Forces\u00a0must only consider (1) the ability of an individual to meet the general occupational standards for service, and (2) the particular military occupational specialty.</p><p>On January 20, 2025, President Donald Trump signed an executive order titled <em>Defending Women from Gender Ideology Extremism and Restoring Biological Truth to the Federal Government</em>, declaring that the United States recognizes two sexes (male and female) and these sexes are not changeable.</p><p>On January 27, 2025, President Donald Trump signed an executive order titled<em> Prioritizing Military Excellence and Readiness</em>, expressing that the policy for troop readiness is inconsistent with gender dysphoria or the use of pronouns that inaccurately reflect an individual\u2019s biological sex. Further, the order directs DOD to update specific guidance documents related to medical standards for military service to reflect the purpose and policy of the order.</p>",
      "updateDate": "2025-08-13",
      "versionCode": "id119hr1543"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1543ih.xml"
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
      "title": "EQUITY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EQUITY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Equal and Uniform Treatment in the Military Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to prohibit discrimination in the Armed Forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:29Z"
    }
  ]
}
```
