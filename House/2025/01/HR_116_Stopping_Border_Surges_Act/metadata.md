# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/116
- Title: Stopping Border Surges Act
- Congress: 119
- Bill type: HR
- Bill number: 116
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-05-13T08:06:06Z
- Update date including text: 2026-05-13T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/116",
    "number": "116",
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
    "title": "Stopping Border Surges Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:06Z",
    "updateDateIncludingText": "2026-05-13T08:06:06Z"
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
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-01-03T16:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:05:30Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "CO"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "GA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "AZ"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "TX"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "SC"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "TX"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "OH"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "WI"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "KY"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "TX"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "SC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "IL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "GA"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "SC"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "FL"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "WV"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "TN"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "PA"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "TN"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "MO"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "AL"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr116ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 116\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo close loopholes in the immigration laws that serve as incentives to aliens to attempt to enter the United States unlawfully, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Stopping Border Surges Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014Unaccompanied Alien Children\nSec. 101. Repatriation of unaccompanied alien children.\nSec. 102. Clarification of standards for family detention.\nSec. 103. Special immigrant juvenile status for immigrants unable to reunite with either parent.\nTitle II\u2014Asylum Reform\nSec. 201. Credible fear interviews.\nSec. 202. Jurisdiction of asylum applications.\nSec. 203. Recording expedited removal and credible fear interviews.\nSec. 204. Safe third country.\nSec. 205. Renunciation of asylum status pursuant to return to home country.\nSec. 206. Notice concerning frivolous asylum applications.\nSec. 207. Anti-fraud investigative work product.\nSec. 208. Clarification of asylum eligibility.\nSec. 209. Application timing.\nSec. 210. Clarification of burden of proof.\nSec. 211. Additional exception.\nSec. 212. Clarification regarding employment eligibility.\nSec. 213. Penalties for asylum fraud.\nSec. 214. Statute of limitations for asylum fraud.\nSec. 215. Technical amendments.\nI\nUnaccompanied Alien Children\n#### 101. Repatriation of unaccompanied alien children\n##### (a) In general\nSection 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby amending the heading to read as follows: Rules for unaccompanied alien children.\u2014 ;\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nin the matter preceding clause (i), by striking who is a national or habitual resident of a country that is contiguous with the United States ;\n**(II)**\nin clause (i), by inserting and at the end;\n**(III)**\nin clause (ii), by striking ; and and inserting a period; and\n**(IV)**\nby striking clause (iii);\n**(iii)**\nin subparagraph (B)\u2014\n**(I)**\nin the matter preceding clause (i), by striking ( 8 U.S.C. 1101 et seq. ) may\u2014 and inserting ( 8 U.S.C. 1101 et seq. )\u2014 ;\n**(II)**\nin clause (i), by inserting before permit such child to withdraw the following: may ; and\n**(III)**\nin clause (ii), by inserting before return such child the following: shall ; and\n**(iv)**\nin subparagraph (C)\u2014\n**(I)**\nby amending the heading to read as follows: Agreements with foreign countries.\u2014 ; and\n**(II)**\nin the matter preceding clause (i), by striking The Secretary of State shall negotiate agreements between the United States and countries contiguous to the United States and inserting The Secretary of State may negotiate agreements between the United States and any foreign country that the Secretary determines appropriate ;\n**(B)**\nby redesignating paragraphs (3) through (5) as paragraphs (4) through (6), respectively, and inserting after paragraph (2) the following:\n(3) Special rules for interviewing unaccompanied alien children An unaccompanied alien child shall be interviewed by an immigration officer with specialized training in interviewing child trafficking victims. ; and\n**(C)**\nin paragraph (6)(D) (as so redesignated)\u2014\n**(i)**\nin the matter preceding clause (i), by striking , except for an unaccompanied alien child from a contiguous country subject to exceptions under subsection (a)(2), and inserting who does not meet the criteria listed in paragraph (2)(A) ; and\n**(ii)**\nin clause (i), by inserting before the semicolon at the end the following: , which shall include a hearing before an immigration judge not later than 14 days after being screened under paragraph (4) ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by inserting before the semicolon the following: believed not to meet the criteria listed in subsection (a)(2)(A) ; and\n**(ii)**\nin subparagraph (B), by inserting before the period the following: and does not meet the criteria listed in subsection (a)(2)(A) ; and\n**(B)**\nin paragraph (3), by striking an unaccompanied alien child in custody shall and all that follows, and inserting the following:\nan unaccompanied alien child in custody\u2014 (A) in the case of a child who does not meet the criteria listed in subsection (a)(2)(A), shall transfer the custody of such child to the Secretary of Health and Human Services not later than 30 days after determining that such child is an unaccompanied alien child who does not meet such criteria; or (B) in the case of child who meets the criteria listed in subsection (a)(2)(A), may transfer the custody of such child to the Secretary of Health and Human Services after determining that such child is an unaccompanied alien child who meets such criteria. ; and\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (3), by inserting at the end the following:\n(D) Information about individuals with whom children are placed (i) Information to be provided to Homeland Security Before placing a child with an individual, the Secretary of Health and Human Services shall provide to the Secretary of Homeland Security, regarding the individual with whom the child will be placed, the following information: (I) The name of the individual. (II) The social security number of the individual, if available. (III) The date of birth of the individual. (IV) The location of the individual\u2019s residence where the child will be placed. (V) The immigration status of the individual, if known. (VI) Contact information for the individual. (ii) Special rule In the case of a child who was apprehended on or after the effective date of this clause, and before the date of the enactment of this subparagraph, who the Secretary of Health and Human Services placed with an individual, the Secretary shall provide the information listed in clause (i) to the Secretary of Homeland Security not later than 90 days after such date of enactment. ; and\n**(B)**\nin paragraph (5)\u2014\n**(i)**\nby inserting after to the greatest extent practicable the following: (at no expense to the Government) ; and\n**(ii)**\nby striking have counsel to represent them and inserting have access to counsel to represent them .\n##### (b) Effective date\nThe amendments made by this section shall apply to any unaccompanied alien child apprehended on or after the date of enactment.\n#### 102. Clarification of standards for family detention\n##### (a) In general\nSection 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 ) is amended by adding at the end the following:\n(j) Construction (1) In general Notwithstanding any other provision of law, judicial determination, consent decree, or settlement agreement, the detention of any alien child who is not an unaccompanied alien child shall be governed by sections 217, 235, 236, and 241 of the Immigration and Nationality Act ( 8 U.S.C. 1187 , 1225, 1226, and 1231). There is no presumption that an alien child who is not an unaccompanied alien child should not be detained, and all such determinations shall be in the discretion of the Secretary of Homeland Security. (2) Release of minors other than unaccompanied aliens In no circumstances shall an alien minor who is not an unaccompanied alien child be released by the Secretary of Homeland Security other than to a parent or legal guardian, who is lawfully present in the United States. (3) Family detention The Secretary of Homeland Security shall\u2014 (A) maintain the care and custody of an alien, during the period during which the charges described in clause (i) are pending, who\u2014 (i) is charged only with a misdemeanor offense under section 275(a) of the Immigration and Nationality Act ( 8 U.S.C. 1325(a) ); and (ii) entered the United States with the alien\u2019s child who has not attained 18 years of age; and (B) detain the alien with the alien\u2019s child. .\n##### (b) Sense of Congress\nIt is the sense of Congress that the amendments in this section to section 235 of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( 8 U.S.C. 1232 ) are intended to satisfy the requirements of the Settlement Agreement in Flores v. Meese, No. 85\u20134544 (C.D. Cal) as approved by the court on January 28, 1997, with respect to its interpretation in Flores v. Johnson, 212 F. Supp. 3d 864 (C.D. Cal. 2015), that the agreement applies to accompanied minors.\n##### (c) Effective date\nThe amendment made by subsection (a) shall take effect on the date of the enactment of this Act and shall apply to all actions that occur before, on, or after the date of the enactment of this Act.\n##### (d) Preemption of State licensing requirements\nNotwithstanding any other provision of law, judicial determination, consent decree, or settlement agreement, no State may require that an immigration detention facility used to detain children who have not attained 18 years of age, or families consisting of one or more of such children and the parents or legal guardians of such children, that is located in that State, be licensed by the State or any political subdivision thereof.\n#### 103. Special immigrant juvenile status for immigrants unable to reunite with either parent\nSection 101(a)(27)(J) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27)(J) ) is amended\u2014\n**(1)**\nin clause (i), by striking , and whose reunification with 1 or both of the immigrant's parents is not viable due to abuse, neglect, abandonment, or a similar basis found under State law ; and\n**(2)**\nin clause (iii)\u2014\n**(A)**\nby striking and at the end of subclause (I);\n**(B)**\nby inserting and at the end of subclause (II); and\n**(C)**\nby adding at the end the following:\n(III) an alien may not be granted special immigrant juvenile status under this subparagraph if his or her reunification with any one parent or legal guardian is not precluded by abuse, neglect, abandonment, or any similar cause under State law; .\nII\nAsylum Reform\n#### 201. Credible fear interviews\nSection 235(b)(1)(B)(v) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1)(B)(v) ) is amended by striking claim and all that follows, and inserting claim, as determined pursuant to section 208(b)(1)(B)(iii), and such other facts as are known to the officer, that the alien could establish eligibility for asylum under section 208, and it is more probable than not that the statements made by, and on behalf of, the alien in support of the alien\u2019s claim are true. .\n#### 202. Jurisdiction of asylum applications\nSection 208(b)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1158 ) is amended by striking subparagraph (C).\n#### 203. Recording expedited removal and credible fear interviews\n##### (a) In general\nThe Secretary of Homeland Security shall establish quality assurance procedures and take steps to effectively ensure that questions by employees of the Department of Homeland Security exercising expedited removal authority under section 235(b) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b) ) are asked in a uniform manner, to the extent possible, and that both these questions and the answers provided in response to them are recorded in a uniform fashion.\n##### (b) Credible fear interview checklists\nThe Secretary of Homeland Security shall provide a checklist of standard questions and concepts to be addressed in all interviews under section 235(b) to immigration officers exercising decision-making authority in such interviews. Such checklists shall be routinely updated to include relevant changes to law and procedures and shall, at a minimum, require that all immigration officers utilizing such checklists provide concise justifications of their decision regardless of whether credible fear was or was not established.\n##### (c) Factors relating to sworn statements\nWhere practicable, any sworn or signed written statement taken of an alien as part of the record of a proceeding under section 235(b)(1)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(1)(A) ) shall be accompanied by a recording of the interview which served as the basis for that sworn statement.\n##### (d) Interpreters\nThe Secretary shall ensure that a competent interpreter, not affiliated with the government of the country from which the alien may claim asylum, is used when the interviewing officer does not speak a language understood by the alien.\n##### (e) Recordings in immigration proceedings\nThere shall be an audio or audio visual recording of interviews of aliens subject to expedited removal. The recording shall be included in the record of proceeding and shall be considered as evidence in any further proceedings involving the alien.\n##### (f) No private right of action\nNothing in this section shall be construed to create any right, benefit, trust, or responsibility, whether substantive or procedural, enforceable in law or equity by a party against the United States, its departments, agencies, instrumentalities, entities, officers, employees, or agents, or any person, nor does this section create any right of review in any administrative, judicial, or other proceeding.\n#### 204. Safe third country\nSection 208(a)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a)(2)(A) ) is amended\u2014\n**(1)**\nby striking if the Attorney General determines and inserting if the Attorney General or the Secretary of Homeland Security determines\u2014 ;\n**(2)**\nby striking that the alien may be and inserting:\n(i) that the alien may be ;\n**(3)**\nby striking removed, pursuant to a bilateral or multilateral agreement, to and inserting removed to ;\n**(4)**\nby inserting , on a case by case basis, before finds that ;\n**(5)**\nby striking the period at the end and inserting ; or ; and\n**(6)**\nby adding at the end the following:\n(ii) that the alien entered, attempted to enter, or arrived in the United States after transiting through at least one country outside the alien\u2019s country of citizenship, nationality, or last lawful habitual residence en route to the United States, unless\u2014 (I) the alien demonstrates that he or she applied for protection from persecution or torture in at least one country outside the alien\u2019s country of citizenship, nationality, or last lawful habitual residence through which the alien transited en route to the United States, and the alien received a final judgement denying the alien protection in each country; (II) the alien demonstrates that he or she was a victim of a severe form of trafficking in which a commercial sex act was induced by force, fraud, or coercion, or in which the person induced to perform such act was under the age of 18 years; or in which the trafficking included the recruitment, harboring, transportation, provision, or obtaining of a person for labor or services through the use of force, fraud, or coercion for the purpose of subjection to involuntary servitude, peonage, debt bondage, or slavery, and was unable to apply for protection from persecution in all countries that alien transited en route to the United States as a result of such severe form of trafficking; or (III) the only countries through which the alien transited en route to the United States were, at the time of the transit, not parties to the 1951 United Nations Convention relating to the Status of Refugees, the 1967 Protocol Relating to the Status of Refugees, or the United Nations Convention against Torture and Other Cruel, Inhuman or Degrading Treatment or Punishment. .\n#### 205. Renunciation of asylum status pursuant to return to home country\n##### (a) In general\nSection 208(c) of the Immigration and Nationality Act ( 8 U.S.C. 1158(c) ) is amended by adding at the end the following new paragraph:\n(4) Renunciation of status pursuant to return to home country (A) In general Except as provided in subparagraph (B), any alien who is granted asylum status under this Act, who, absent changed country conditions, subsequently returns to the country of such alien\u2019s nationality or, in the case of an alien having no nationality, returns to any country in which such alien last habitually resided, and who applied for such status because of persecution or a well-founded fear of persecution in that country on account of race, religion, nationality, membership in a particular social group, or political opinion, shall have his or her status terminated. (B) Waiver The Secretary has discretion to waive subparagraph (A) if it is established to the satisfaction of the Secretary that the alien had a compelling reason for the return. The waiver may be sought prior to departure from the United States or upon return. .\n##### (b) Conforming amendment\nSection 208(c)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1158(c)(3) ) is amended by inserting after paragraph (2) the following: or (4) .\n#### 206. Notice concerning frivolous asylum applications\n##### (a) In general\nSection 208(d)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1158(d)(4) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by inserting the Secretary of Homeland Security or before the Attorney General ;\n**(2)**\nin subparagraph (A), by striking and of the consequences, under paragraph (6), of knowingly filing a frivolous application for asylum; and and inserting a semicolon;\n**(3)**\nin subparagraph (B), by striking the period and inserting ; and ; and\n**(4)**\nby adding at the end the following:\n(C) ensure that a written warning appears on the asylum application advising the alien of the consequences of filing a frivolous application and serving as notice to the alien of the consequence of filing a frivolous application. .\n##### (b) Conforming amendment\nSection 208(d)(6) of the Immigration and Nationality Act ( 8 U.S.C. 1158(d)(6) ) is amended by striking If the and all that follows and inserting:\n(A) If the Secretary of Homeland Security or the Attorney General determines that an alien has knowingly made a frivolous application for asylum and the alien has received the notice under paragraph (4)(C), the alien shall be permanently ineligible for any benefits under this chapter, effective as the date of the final determination of such an application. (B) An application is frivolous if the Secretary of Homeland Security or the Attorney General determines, consistent with subparagraph (C), that\u2014 (i) it is so insufficient in substance that it is clear that the applicant knowingly filed the application solely or in part to delay removal from the United States, to seek employment authorization as an applicant for asylum pursuant to regulations issued pursuant to paragraph (2), or to seek issuance of a Notice to Appear in order to pursue Cancellation of Removal under section 240A(b); or (ii) any of the material elements are knowingly fabricated. (C) In determining that an application is frivolous, the Secretary or the Attorney General, must be satisfied that the applicant, during the course of the proceedings, has had sufficient opportunity to clarify any discrepancies or implausible aspects of the claim. (D) For purposes of this section, a finding that an alien filed a frivolous asylum application shall not preclude the alien from seeking withholding of removal under section 241(b)(3) or protection pursuant to the Convention Against Torture. .\n#### 207. Anti-fraud investigative work product\n##### (a) Asylum credibility determinations\nSection 208(b)(1)(B)(iii) of the Immigration and Nationality Act ( 8 U.S.C. 1158(b)(1)(B)(iii) ) is amended by inserting after all relevant factors the following: , including statements made to, and investigative reports prepared by, immigration authorities and other government officials .\n##### (b) Relief for removal credibility determinations\nSection 240(c)(4)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(c)(4)(C) ) is amended by inserting after all relevant factors the following: , including statements made to, and investigative reports prepared by, immigration authorities and other government officials .\n#### 208. Clarification of asylum eligibility\n##### (a) In general\nSection 208(b)(1)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1158(b)(1)(A) ) is amended by inserting after section 101(a)(42)(A) the following: and is eligible to apply for asylum under subsection (a) .\n##### (b) Place of arrival\nSection 208(a)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a)(1) ) is amended\u2014\n**(1)**\nby striking or who arrives in the United States (whether or not at a designated port of arrival and including an alien who is brought to the United States after having been interdicted in international or United States waters), ; and\n**(2)**\nby inserting after United States the following: and has arrived in the United States at a port of entry, .\n#### 209. Application timing\nSection 208(a)(2)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a)(2)(B) ) is amended by striking 1 year and inserting 6 months .\n#### 210. Clarification of burden of proof\nSection 208(b)(1)(B)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1158(b)(1)(B)(i) ) is amended by striking at least one and inserting the .\n#### 211. Additional exception\nSection 208(b)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1158(b)(2)(A) ) is amended\u2014\n**(1)**\nin clause (v), by striking or at the end;\n**(2)**\nin clause (vi), by striking the period and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(vii) there are reasonable grounds for concluding the alien could avoid persecution by relocating to another part of the alien\u2019s country of nationality or, if stateless, another part of the alien\u2019s country of last habitual residence. .\n#### 212. Clarification regarding employment eligibility\nSection 208(d)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1158(d)(2) ) is amended\u2014\n**(1)**\nby striking 180 days \u201d and inserting 1 year ; and\n**(2)**\nby inserting and the authorization shall expire 6 months after the date of issuance before the period at the end.\n#### 213. Penalties for asylum fraud\nSection 1001 of title 18, United States Code, is amended by inserting at the end of the paragraph\u2014\n(d) Whoever, in any matter before the Secretary of Homeland Security or the Attorney General pertaining to asylum under section 208 of the Immigration and Nationality Act or withholding of removal under section 241(b)(3) of such Act, knowingly and willfully\u2014 (1) makes any materially false, fictitious, or fraudulent statement or representation; or (2) makes or uses any false writings or document knowing the same to contain any materially false, fictitious, or fraudulent statement or entry, shall be fined under this title or imprisoned not more than 10 years, or both. .\n#### 214. Statute of limitations for asylum fraud\nSection 3291 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking 1544, and inserting 1544, and section 1546, ; and\n**(2)**\nby striking offense. and inserting offense or within 10 years after the fraud is discovered. .\n#### 215. Technical amendments\nSection 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)(D), by inserting Secretary of Homeland Security or the before Attorney General ; and\n**(B)**\nin paragraph (3), by inserting Secretary of Homeland Security or the before Attorney General ;\n**(2)**\nin subsection (b)(2), by inserting Secretary of Homeland Security or the before Attorney General each place such term appears;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by striking Attorney General each place such term appears and inserting Secretary of Homeland Security ;\n**(B)**\nin paragraph (2), in the matter preceding subparagraph (A), by inserting Secretary of Homeland Security or the before Attorney General ; and\n**(C)**\nin paragraph (3), by inserting Secretary of Homeland Security or the before Attorney General ; and\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by inserting Secretary of Homeland Security or the before Attorney General each place such term appears;\n**(B)**\nin paragraph (2), by striking Attorney General and inserting Secretary of Homeland Security ; and\n**(C)**\nin paragraph (5)\u2014\n**(i)**\nin subparagraph (A), by striking Attorney General and inserting Secretary of Homeland Security ; and\n**(ii)**\nin subparagraph (B), by inserting Secretary of Homeland Security or the before Attorney General .",
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
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "61",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring United Families at the Border Act",
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
            "name": "Administrative remedies",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Foreign labor",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Foreign language and bilingual programs",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Immigrant health and welfare",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "International law and treaties",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-03T20:18:41Z"
          },
          {
            "name": "Refugees, asylum, displaced persons",
            "updateDate": "2025-09-03T20:18:40Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-09-03T20:18:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-06T20:53:47Z"
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
          "measure-id": "id119hr116",
          "measure-number": "116",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr116v00",
            "update-date": "2025-02-26"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong> Stopping Border Surges Act </strong></p><p>This bill modifies immigration law provisions relating to unaccompanied alien minors and to asylum seekers.</p><p>The bill requires the Department of Homeland Security (DHS) to repatriate certain unaccompanied, inadmissible alien children, generally those not at risk of being trafficking victims nor having a fear of persecution. Currently, only inadmissible unaccompanied aliens from neighboring countries are subject to repatriation, and DHS has discretion whether to repatriate.</p><p>When the Department of Health and Human Services releases an unaccompanied child to an individual, it shall provide DHS with certain information about that individual, including Social Security number and immigration status.</p><p>The bill requires a stricter standard to find a credible fear of persecution and imposes additional rules on credible fear interviews.</p><p>If an alien is granted asylum because of fear of persecution in a country, the alien shall be deemed to have renounced asylum status by returning to that country, if there has been no change in the country's conditions.</p><p>The bill also (1) expands the definition of what constitutes a frivolous asylum application, (2) imposes additional limitations on eligibility for asylum, (3) shortens the deadline for applying for asylum, and (4) extends the time period an alien seeking asylum must wait before receiving employment authorization.</p><p>Any individual who knowingly and willfully makes materially false statements or uses fraudulent documents in asylum-related proceedings shall be fined or imprisoned up to 10 years, or both.</p>"
        },
        "title": "Stopping Border Surges Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr116.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong> Stopping Border Surges Act </strong></p><p>This bill modifies immigration law provisions relating to unaccompanied alien minors and to asylum seekers.</p><p>The bill requires the Department of Homeland Security (DHS) to repatriate certain unaccompanied, inadmissible alien children, generally those not at risk of being trafficking victims nor having a fear of persecution. Currently, only inadmissible unaccompanied aliens from neighboring countries are subject to repatriation, and DHS has discretion whether to repatriate.</p><p>When the Department of Health and Human Services releases an unaccompanied child to an individual, it shall provide DHS with certain information about that individual, including Social Security number and immigration status.</p><p>The bill requires a stricter standard to find a credible fear of persecution and imposes additional rules on credible fear interviews.</p><p>If an alien is granted asylum because of fear of persecution in a country, the alien shall be deemed to have renounced asylum status by returning to that country, if there has been no change in the country's conditions.</p><p>The bill also (1) expands the definition of what constitutes a frivolous asylum application, (2) imposes additional limitations on eligibility for asylum, (3) shortens the deadline for applying for asylum, and (4) extends the time period an alien seeking asylum must wait before receiving employment authorization.</p><p>Any individual who knowingly and willfully makes materially false statements or uses fraudulent documents in asylum-related proceedings shall be fined or imprisoned up to 10 years, or both.</p>",
      "updateDate": "2025-02-26",
      "versionCode": "id119hr116"
    },
    "title": "Stopping Border Surges Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong> Stopping Border Surges Act </strong></p><p>This bill modifies immigration law provisions relating to unaccompanied alien minors and to asylum seekers.</p><p>The bill requires the Department of Homeland Security (DHS) to repatriate certain unaccompanied, inadmissible alien children, generally those not at risk of being trafficking victims nor having a fear of persecution. Currently, only inadmissible unaccompanied aliens from neighboring countries are subject to repatriation, and DHS has discretion whether to repatriate.</p><p>When the Department of Health and Human Services releases an unaccompanied child to an individual, it shall provide DHS with certain information about that individual, including Social Security number and immigration status.</p><p>The bill requires a stricter standard to find a credible fear of persecution and imposes additional rules on credible fear interviews.</p><p>If an alien is granted asylum because of fear of persecution in a country, the alien shall be deemed to have renounced asylum status by returning to that country, if there has been no change in the country's conditions.</p><p>The bill also (1) expands the definition of what constitutes a frivolous asylum application, (2) imposes additional limitations on eligibility for asylum, (3) shortens the deadline for applying for asylum, and (4) extends the time period an alien seeking asylum must wait before receiving employment authorization.</p><p>Any individual who knowingly and willfully makes materially false statements or uses fraudulent documents in asylum-related proceedings shall be fined or imprisoned up to 10 years, or both.</p>",
      "updateDate": "2025-02-26",
      "versionCode": "id119hr116"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr116ih.xml"
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
      "title": "Stopping Border Surges Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T13:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Border Surges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T13:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To close loopholes in the immigration laws that serve as incentives to aliens to attempt to enter the United States unlawfully, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T13:18:19Z"
    }
  ]
}
```
