# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/61?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/61
- Title: Ensuring United Families at the Border Act
- Congress: 119
- Bill type: HR
- Bill number: 61
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-09-02T16:32:24Z
- Update date including text: 2025-09-02T16:32:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/61",
    "number": "61",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Ensuring United Families at the Border Act",
    "type": "HR",
    "updateDate": "2025-09-02T16:32:24Z",
    "updateDateIncludingText": "2025-09-02T16:32:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:07:35Z",
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
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "MO"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr61ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 61\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Burlison , Mr. Crane , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 to clarify the standards for family detention, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring United Families at the Border Act .\n#### 2. Clarification of standards for family detention\n##### (a) In general\nSection 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 ) is amended by adding at the end the following:\n(j) Construction (1) In general Notwithstanding any other provision of law, judicial determination, consent decree, or settlement agreement, the detention of any alien child who is not an unaccompanied alien child shall be governed by sections 217, 235, 236, and 241 of the Immigration and Nationality Act ( 8 U.S.C. 1187 , 1225, 1226, and 1231). There is no presumption that an alien child who is not an unaccompanied alien child should not be detained. (2) Family detention The Secretary of Homeland Security shall\u2014 (A) maintain the care and custody of an alien, during the period during which the charges described in clause (i) are pending, who\u2014 (i) is charged only with a misdemeanor offense under section 275(a) of the Immigration and Nationality Act ( 8 U.S.C. 1325(a) ); and (ii) entered the United States with the alien\u2019s child who has not attained 18 years of age; and (B) detain the alien with the alien\u2019s child. .\n##### (b) Sense of Congress\nIt is the sense of Congress that the amendments in this section to section 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 ) are intended to satisfy the requirements of the Settlement Agreement in Flores v. Meese, No. 85\u20134544 (C.D. Cal) as approved by the court on January 28, 1997, with respect to its interpretation in Flores v. Johnson, 212 F. Supp. 3d 864 (C.D. Cal. 2015), that the agreement applies to accompanied minors.\n##### (c) Effective date\nThe amendment made by subsection (a) shall take effect on the date of the enactment of this Act and shall apply to all actions that occur before, on, or after the date of the enactment of this Act.\n##### (d) Preemption of State licensing requirements\nNotwithstanding any other provision of law, judicial determination, consent decree, or settlement agreement, no State may require that an immigration detention facility used to detain children who have not attained 18 years of age, or families consisting of one or more of such children and the parents or legal guardians of such children, that is located in that State, be licensed by the State or any political subdivision thereof.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "116",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stopping Border Surges Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-09-02T16:31:16Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2025-09-02T16:31:30Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-09-02T16:30:31Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-09-02T16:31:37Z"
          },
          {
            "name": "Immigrant health and welfare",
            "updateDate": "2025-09-02T16:31:55Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-09-02T16:32:00Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-02T16:32:19Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-09-02T16:32:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-03T15:00:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr61",
          "measure-number": "61",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr61v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Ensuring United Families at the Border Act</strong></p><p>This bill addresses the treatment of children who are non-U.S. nationals (<em>aliens</em> under federal law), including by statutorily establishing that there is no presumption that such a child (other than an unaccompanied child) should not be detained for immigration purposes.</p><p>Specifically, the bill states that the detention of such minors shall be governed by specified sections of the Immigration and Nationality Act and not any other provision of law, judicial ruling, or settlement agreement.</p><p>(A 1997 settlement agreement, commonly known as the <em>Flores</em> agreement, imposes requirements relating to the treatment of detained alien minors, including requiring such minors to be released or placed in a nonsecure facility after a certain amount of time in detention.)</p><p>If an adult enters the United States unlawfully with their child, the Department of Homeland Security must detain the adult and child together if the only criminal charge against the adult is a misdemeanor for unlawful entry.</p><p>This bill also prohibits states from imposing licensing requirements on immigration detention facilities used to detain minors or families with minors.</p>"
        },
        "title": "Ensuring United Families at the Border Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr61.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring United Families at the Border Act</strong></p><p>This bill addresses the treatment of children who are non-U.S. nationals (<em>aliens</em> under federal law), including by statutorily establishing that there is no presumption that such a child (other than an unaccompanied child) should not be detained for immigration purposes.</p><p>Specifically, the bill states that the detention of such minors shall be governed by specified sections of the Immigration and Nationality Act and not any other provision of law, judicial ruling, or settlement agreement.</p><p>(A 1997 settlement agreement, commonly known as the <em>Flores</em> agreement, imposes requirements relating to the treatment of detained alien minors, including requiring such minors to be released or placed in a nonsecure facility after a certain amount of time in detention.)</p><p>If an adult enters the United States unlawfully with their child, the Department of Homeland Security must detain the adult and child together if the only criminal charge against the adult is a misdemeanor for unlawful entry.</p><p>This bill also prohibits states from imposing licensing requirements on immigration detention facilities used to detain minors or families with minors.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr61"
    },
    "title": "Ensuring United Families at the Border Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Ensuring United Families at the Border Act</strong></p><p>This bill addresses the treatment of children who are non-U.S. nationals (<em>aliens</em> under federal law), including by statutorily establishing that there is no presumption that such a child (other than an unaccompanied child) should not be detained for immigration purposes.</p><p>Specifically, the bill states that the detention of such minors shall be governed by specified sections of the Immigration and Nationality Act and not any other provision of law, judicial ruling, or settlement agreement.</p><p>(A 1997 settlement agreement, commonly known as the <em>Flores</em> agreement, imposes requirements relating to the treatment of detained alien minors, including requiring such minors to be released or placed in a nonsecure facility after a certain amount of time in detention.)</p><p>If an adult enters the United States unlawfully with their child, the Department of Homeland Security must detain the adult and child together if the only criminal charge against the adult is a misdemeanor for unlawful entry.</p><p>This bill also prohibits states from imposing licensing requirements on immigration detention facilities used to detain minors or families with minors.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr61"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr61ih.xml"
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
      "title": "Ensuring United Families at the Border Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T07:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ensuring United Families at the Border Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T07:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 to clarify the standards for family detention, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T07:48:35Z"
    }
  ]
}
```
