# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2589
- Title: Expanding the VOTE Act
- Congress: 119
- Bill type: S
- Bill number: 2589
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-02-18T22:17:39Z
- Update date including text: 2026-02-18T22:17:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2589",
    "number": "2589",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expanding the VOTE Act",
    "type": "S",
    "updateDate": "2026-02-18T22:17:39Z",
    "updateDateIncludingText": "2026-02-18T22:17:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T19:24:36Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "CT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NM"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NY"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "WI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-31",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2589is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2589\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Padilla (for himself, Ms. Klobuchar , Ms. Warren , Mr. Markey , Mr. Schiff , Mr. Merkley , Mr. Blumenthal , Mr. Luj\u00e1n , Mrs. Gillibrand , Ms. Smith , Mr. Kim , Ms. Baldwin , Mr. Sanders , Mr. Wyden , Mr. Booker , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo modify certain notice requirements, to study certain election requirements, to clarify certain election requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act .\n#### 2. Language minority notice requirements\nSection 203 of the Voting Rights Act of 1965 ( 52 U.S.C. 10503 ) is amended\u2014\n**(1)**\nby amending subsection (b)(3)(A) to read as follows:\n(A) the term voting materials \u2014 (i) means registration or voting notices, forms, instructions, assistance, or other materials or information relating to the electoral process, including ballots; and (ii) includes digital and printed material or information produced relating to the electoral process; ;\n**(2)**\nby redesignating subsection (e) as subsection (g); and\n**(3)**\nby inserting after subsection (d) the following new subsections:\n(e) Responsibility of States providing voting materials in covered political subdivisions The prohibition under subsection (b) shall apply to any State that provides voting materials to a political subdivision subject to such prohibition. (f) Notice The Attorney General shall submit a notice of the prohibition of subsection (b), and the threshold at which such prohibition applies, to each State or political subdivision that is\u2014 (1) below the threshold requirement under subclause (II) of subsection (b)(2)(A)(i) by not more than 1,000; or (2) below the threshold requirement under subclause (I) or (III) of subsection (b)(2)(A)(i) by not more than 0.5 percent. .\n#### 3. Provisions related to American Indian and Alaska Native languages\nSection 203 of the Voting Rights Act of 1965 ( 52 U.S.C. 10503 ), as amended by section 2, is further amended\u2014\n**(1)**\nin subsection (b)(3)(C), by striking 1990 and inserting most recent ; and\n**(2)**\nby striking subsection (c) and inserting the following:\n(c) Provision of voting materials in the language of a minority group (1) In general Subject to paragraph (2), whenever any State or political subdivision subject to the prohibition of subsection (b) provides any registration or voting notices, forms, instructions, assistance, or other materials or information relating to the electoral process, including ballots, it shall provide them in the language of the applicable minority group as well as in the English language. (2) Exceptions (A) When written American Indian and Alaska Native translations for voters are not required In the case of a minority group that is American Indian or Alaska Native, if the Tribal government of that minority group has notified the Attorney General that the language is unwritten or the Tribal government does not want a written translation, a State or political subdivision subject to the prohibition of subsection (b) shall only be required to furnish that minority group, in the covered language, oral instructions, assistance, translation of voting materials, and other information relating to registration and voting. (B) Other minority groups with unwritten language In the case of a minority group that is not American Indian or Alaska Native, if the language of that minority group is unwritten, a State or political subdivision subject to the prohibition of subsection (b) shall only be required to furnish that minority group, in the covered language, oral instructions, assistance, translation of voting materials, and other information relating to registration and voting. (3) Written translations for election workers Notwithstanding paragraph (2), a State or political division subject to the prohibition of subsection (b) shall provide written translations of all voting materials, with the consent of any applicable Tribal government, to election workers to ensure that the translations from English to the language of a minority group are complete, accurate, and uniform. (4) Tribal government defined In this subsection, the term Tribal government means the recognized governing body of any Indian or Alaska Native Tribe, band, nation, pueblo, village, community, component band, or component reservation, individually identified (including parenthetically) in the list published most recently as of the date of enactment of the Expanding the VOTE Act pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ). .\n#### 4. Grants to jurisdictions to incentivize the provision of voting materials in languages not triggering Section 203 coverage in applying jurisdiction\n##### (a) Availability of grants\n**(1) In general**\nThe Election Assistance Commission (in this section, referred to as the Commission ) shall make incentive grants under subsection (b) to States and political subdivisions to assist the States and political subdivisions in providing voting materials during an election cycle in the language of a covered language minority group.\n**(2) Application required**\nIn order to receive a grant under this section, a State or political subdivision shall submit to the Commission, at such time and in such form as the Commission may require, an application containing such information and assurances as the Commission may require, such as a plan for the State or political subdivision to engage stakeholders with a demonstrated experience of serving the relevant covered language minority group.\n##### (b) Incentive grants\n**(1) Use of funds**\nThe Commission shall make an incentive grant under this subsection to a State or political subdivision to cover the reasonable costs incurred by the State or political subdivision in providing voting materials in the language of a covered language minority group for an election cycle.\n**(2) Continuation of provision of materials for groups in succeeding election cycles**\nIf a State or political subdivision receives an incentive grant with respect to a covered language minority group for an election cycle, the State or political subdivision will certify to the Commission that the State or political subdivision will continue to provide voting materials in the language of that covered language minority group for each succeeding election cycle unless the population of the group during the succeeding cycle has dropped by 0.5 percent or more from the population of the group during the first election cycle for which the State or political subdivision received an incentive grant with respect to the group.\n**(3) Prohibiting multiple grants for same language minority group**\nIf a State or political subdivision receives an incentive grant with respect to a covered language minority group, the State or subdivision may not receive another incentive grant with respect to that same covered language minority group.\n##### (c) Definitions\nIn this section\u2014\n**(1)**\nthe term covered language minority group \u2014\n**(A)**\nmeans, with respect to a State or political subdivision, the members of a single language minority who do not meet the requirements of clause (i) or (ii) of section 203(b)(2)(A) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(2)(A) ); and\n**(B)**\nincludes the language minorities described in section 203(g) of such Act ( 52 U.S.C. 10503(g) ) and any other language minority;\n**(2)**\nthe term election cycle means the period which begins on the day after the date of a regularly scheduled general election for Federal office and which ends on the date of the next regularly scheduled general election for Federal office;\n**(3)**\nthe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, American Samoa, Guam, and the Commonwealth of the Northern Mariana Islands; and\n**(4)**\nthe term voting materials has the meaning given under section 203(b)(3)(A) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(3)(A) ).\n##### (d) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $15,000,000, to remain available until expended.\n#### 5. Study on certain language minority notice requirements\n##### (a) In general\nThe Comptroller General of the United States, in consultation with the Director of the Census, the Attorney General, and the Election Assistance Commission, shall conduct a study on the impact of\u2014\n**(1)**\nreducing the threshold requirement\u2014\n**(A)**\nunder subclause (II) of section 203(b)(2)(A)(i) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(2)(A)(i) ) to 7,500 and 5,000, respectively; and\n**(B)**\nunder subclause (I) or (III) of section 203(b)(2)(A)(i) of the Voting Rights Act of 1965 ( 52 U.S.C. 10503(b)(2)(A)(i) ) to 4 percent, 3 percent, 2.5 percent, and 2 percent, respectively; and\n**(2)**\nexpanding the definition of the term language minorities to include native speakers of Arabic, French and Haitian Creole, and any other language that the Comptroller General determines to be appropriate.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the findings of the study conducted under subsection (a).",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-08-05",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4917",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expanding the VOTE Act",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-15T18:07:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
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
          "measure-id": "id119s2589",
          "measure-number": "2589",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2026-02-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2589v00",
            "update-date": "2026-02-18"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act</strong></p><p>This bill expands access to voting materials for individuals with limited proficiency in the English language.</p><p>Section 203 of the Voting Rights Act of 1965 (VRA) requires covered states and political subdivisions to provide voting materials and other language assistance to\u00a0persons who are American Indian, Asian American, Alaskan Natives, or of Spanish heritage and\u00a0whose ability to speak or understand English limits electoral participation. A state or political subdivision that is subject to Section 203 is prohibited from providing English-only voting materials in an election. Among other requirements, this bill (1) requires the Department of Justice to issue a notice of prohibition, including the trigger threshold at which the prohibition applies, to certain states and political subdivisions; and (2) requires covered states and political subdivisions to provide written translations of all voting materials, with the consent of any applicable tribal government, to election workers.</p><p>Additionally, the bill requires the Election Assistance Commission to make incentive grants for states and political subdivisions to provide translated voting materials.</p><p>The bill also directs the Government Accountability Office to study and report on the impact of (1) reducing the threshold requirement under Section 203 of the VRA, and (2) expanding the definition of\u00a0<em>language minorities</em> to include native speakers of additional languages.</p>"
        },
        "title": "Expanding the VOTE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2589.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act</strong></p><p>This bill expands access to voting materials for individuals with limited proficiency in the English language.</p><p>Section 203 of the Voting Rights Act of 1965 (VRA) requires covered states and political subdivisions to provide voting materials and other language assistance to\u00a0persons who are American Indian, Asian American, Alaskan Natives, or of Spanish heritage and\u00a0whose ability to speak or understand English limits electoral participation. A state or political subdivision that is subject to Section 203 is prohibited from providing English-only voting materials in an election. Among other requirements, this bill (1) requires the Department of Justice to issue a notice of prohibition, including the trigger threshold at which the prohibition applies, to certain states and political subdivisions; and (2) requires covered states and political subdivisions to provide written translations of all voting materials, with the consent of any applicable tribal government, to election workers.</p><p>Additionally, the bill requires the Election Assistance Commission to make incentive grants for states and political subdivisions to provide translated voting materials.</p><p>The bill also directs the Government Accountability Office to study and report on the impact of (1) reducing the threshold requirement under Section 203 of the VRA, and (2) expanding the definition of\u00a0<em>language minorities</em> to include native speakers of additional languages.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119s2589"
    },
    "title": "Expanding the VOTE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expanding the Voluntary Opportunities for Translations in Elections Act or the Expanding the VOTE Act</strong></p><p>This bill expands access to voting materials for individuals with limited proficiency in the English language.</p><p>Section 203 of the Voting Rights Act of 1965 (VRA) requires covered states and political subdivisions to provide voting materials and other language assistance to\u00a0persons who are American Indian, Asian American, Alaskan Natives, or of Spanish heritage and\u00a0whose ability to speak or understand English limits electoral participation. A state or political subdivision that is subject to Section 203 is prohibited from providing English-only voting materials in an election. Among other requirements, this bill (1) requires the Department of Justice to issue a notice of prohibition, including the trigger threshold at which the prohibition applies, to certain states and political subdivisions; and (2) requires covered states and political subdivisions to provide written translations of all voting materials, with the consent of any applicable tribal government, to election workers.</p><p>Additionally, the bill requires the Election Assistance Commission to make incentive grants for states and political subdivisions to provide translated voting materials.</p><p>The bill also directs the Government Accountability Office to study and report on the impact of (1) reducing the threshold requirement under Section 203 of the VRA, and (2) expanding the definition of\u00a0<em>language minorities</em> to include native speakers of additional languages.</p>",
      "updateDate": "2026-02-18",
      "versionCode": "id119s2589"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2589is.xml"
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
      "title": "Expanding the VOTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanding the VOTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expanding the Voluntary Opportunities for Translations in Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify certain notice requirements, to study certain election requirements, to clarify certain election requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:22Z"
    }
  ]
}
```
