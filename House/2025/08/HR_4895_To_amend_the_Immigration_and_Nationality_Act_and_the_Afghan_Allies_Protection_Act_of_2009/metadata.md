# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4895?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4895
- Title: Afghan Adjustment Act
- Congress: 119
- Bill type: HR
- Bill number: 4895
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-12-05T21:58:57Z
- Update date including text: 2025-12-05T21:58:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4895",
    "number": "4895",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Afghan Adjustment Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:58:57Z",
    "updateDateIncludingText": "2025-12-05T21:58:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:05:45Z",
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
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CO"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "AZ"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "FL"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "NE"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "IA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "WA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "TX"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NJ"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "AZ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "NY"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "AZ"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4895ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4895\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mrs. Miller-Meeks (for herself, Mr. Crow , Mr. Ciscomani , Mr. Auchincloss , Ms. Salazar , Ms. Houlahan , Mr. Bacon , Ms. Lofgren , Mr. Nunn of Iowa , Mr. Moulton , Mr. Baumgartner , and Mr. Bera ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act and the Afghan Allies Protection Act of 2009, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Afghan Adjustment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on the Judiciary of the Senate;\n**(B)**\nthe Committee on Foreign Relations of the Senate;\n**(C)**\nthe Committee on Armed Services of the Senate;\n**(D)**\nthe Committee on Appropriations of the Senate;\n**(E)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives;\n**(G)**\nthe Committee on Foreign Affairs of the House of Representatives;\n**(H)**\nthe Committee on Armed Services of the House of Representatives;\n**(I)**\nthe Committee on Appropriations of the House of Representatives; and\n**(J)**\nthe Committee on Homeland Security of the House of Representatives.\n**(2) Immigration laws**\nThe term immigration laws has the meaning given such term in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) ).\n**(3) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n**(4) Special immigrant status**\nThe term special immigrant status means special immigrant status provided under\u2014\n**(A)**\nthe Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note; Public Law 111\u20138 );\n**(B)**\nsection 1059 of the National Defense Authorization Act for Fiscal Year 2006 ( 8 U.S.C. 1101 note; Public Law 109\u2013163 ); or\n**(C)**\nsubparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ), as added by section 7(a).\n**(5) Specified application**\nThe term specified application means\u2014\n**(A)**\na pending, documentarily complete application for special immigrant status; and\n**(B)**\na case in processing in the United States Refugee Admissions Program for an individual who has received a Priority 1 or Priority 2 referral to such program.\n**(6) United States Refugee Admissions Program**\nThe term United States Refugee Admissions Program means the program to resettle refugees in the United States pursuant to the authorities provided in sections 101(a)(42), 207, and 412 of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(42) , 1157, and 1522).\n#### 3. Support for Afghan allies outside the United States\n##### (a) Response to congressional inquiries\nThe Secretary of State shall respond to inquiries by Members of Congress regarding the status of a specified application submitted by, or on behalf of, a national of Afghanistan, including any information that has been provided to the applicant, in accordance with section 222(f) of the Immigration and Nationality Act ( 8 U.S.C. 1202(f) ).\n##### (b) Office in lieu of embassy\nDuring the period in which there is no operational United States embassy in Afghanistan, the Secretary of State shall designate an appropriate office within the Department of State\u2014\n**(1)**\nto review specified applications submitted by nationals of Afghanistan residing in Afghanistan, including by conducting any required interviews;\n**(2)**\nto issue visas or other travel documents to such nationals, in accordance with the immigration laws;\n**(3)**\nto provide services to such nationals, to the greatest extent practicable, that would normally be provided by an embassy; and\n**(4)**\nto carry out any other function the Secretary of State considers necessary.\n#### 4. Conditional permanent resident status for eligible individuals\n##### (a) Definitions\nIn this section:\n**(1) Conditional permanent resident status**\nThe term conditional permanent resident status means conditional permanent resident status under section 216 and 216A of the Immigration and Nationality Act ( 8 U.S.C. 1186a , 1186b), subject to the provisions of this section.\n**(2) Eligible individual**\nThe term eligible individual means an alien who\u2014\n**(A)**\nis present in the United States;\n**(B)**\nis a citizen or national of Afghanistan or, in the case of an alien having no nationality, is a person who last habitually resided in Afghanistan;\n**(C)**\nhas not been granted permanent resident status;\n**(D)**\n**(i)**\nwas inspected and admitted to the United States on or before the date of the enactment of this Act; or\n**(ii)**\nwas paroled into the United States during the period beginning on July 30, 2021, and ending on the date of the enactment of this Act, provided that\u2014\n**(I)**\nsuch parole has not been terminated by the Secretary upon written notice; and\n**(II)**\nthe alien did not enter the United States at a location between ports of entry along the southwest land border; and\n**(E)**\nis admissible to the United States as an immigrant under the applicable immigration laws, including eligibility for waivers of grounds of inadmissibility to the extent provided by the immigration laws and the terms of this section.\n##### (b) Conditional permanent resident status for eligible individuals\n**(1) Adjustment of status to conditional permanent resident status**\nBeginning on the date of the enactment of this Act, the Secretary\u2014\n**(A)**\nmay adjust the status of each eligible individual to that of an alien lawfully admitted for permanent residence status, subject to the procedures established by the Secretary to determine eligibility for conditional permanent resident status; and\n**(B)**\nshall create for each eligible individual who is granted adjustment of status under this section a record of admission to such status as of the date on which the eligible individual was initially inspected and admitted or paroled into the United States, or July 30, 2021, whichever is later,\n8 U.S.C. 1182\n**(2) Conditional basis**\nAn individual who obtains lawful permanent resident status under this section shall be considered, at the time of obtaining the status of an alien lawfully admitted for permanent residence, to have obtained such status on a conditional basis subject to the provisions of this section.\n##### (c) Conditional permanent resident status described\n**(1) Assessment**\n**(A) In general**\nBefore granting conditional permanent resident status to an eligible individual under subsection (b)(1), the Secretary shall conduct an assessment with respect to the eligible individual, which shall be equivalent in rigor to the assessment conducted with respect to refugees admitted to the United States through the United States Refugee Admissions Program, for the purpose of determining whether the eligible individual is inadmissible under any ground of inadmissibility under section 212 (other than subsection (a)(4)) of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) and is not eligible for a waiver of such grounds of inadmissibility under paragraph (2)(C) or the immigration laws.\n**(B) Consultation**\nIn conducting an assessment under subparagraph (A), the Secretary may consult with the head of any other relevant agency and review the holdings of any such agency.\n**(2) Removal of conditions**\n**(A) In general**\nNot earlier than the date described in subparagraph (B), the Secretary may remove the conditional basis of the status of an individual granted conditional permanent resident status under this section unless the Secretary determines, on a case-by-case basis, that such individual is inadmissible under any ground of inadmissibility under paragraph (2) or (3) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ), and is not eligible for a waiver of such grounds of inadmissibility under subparagraph (C) or the immigration laws.\n**(B) Date described**\nThe date described in this subparagraph is the earlier of\u2014\n**(i)**\nthe date that is 4 years after the date on which the individual was admitted or paroled into the United States; or\n**(ii)**\nJuly 1, 2027.\n**(C) Waiver**\n**(i) In general**\nExcept as provided in clause (ii), to determine eligibility for conditional permanent resident status under subsection (b) or removal of conditions under this paragraph, the Secretary may waive the application of the grounds of inadmissibility under section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) for humanitarian purposes or to ensure family unity.\n**(ii) Exceptions**\nThe Secretary may not waive under clause (i) the application of subparagraphs (C) through (E) and (G) through (H) of paragraph (2), or paragraph (3), of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ).\n**(iii) Rule of construction**\nNothing in this subparagraph may be construed to expand or limit any other waiver authority applicable under the immigration laws to an individual who is otherwise eligible for adjustment of status.\n**(D) Timeline**\nNot later than 180 days after the date described in subparagraph (B), the Secretary shall, to the greatest extent practicable, remove conditions as to all individuals granted conditional permanent resident status under this section who are eligible for removal of conditions.\n**(3) Treatment of conditional basis of status period for purposes of naturalization**\nAn individual in conditional permanent resident status under this section shall be considered\u2014\n**(A)**\nto have been admitted to the United States as an alien lawfully admitted for permanent residence; and\n**(B)**\nto be present in the United States as an alien lawfully admitted to the United States for permanent residence, provided that, no alien granted conditional permanent resident status shall be naturalized unless the alien\u2019s conditions have been removed under this section.\n##### (d) Termination of conditional permanent resident status\nConditional permanent resident status shall terminate on, as applicable\u2014\n**(1)**\nthe date on which the Secretary removes the conditions pursuant to subsection (c)(2), on which date the alien shall be lawfully admitted for permanent residence without conditions;\n**(2)**\nthe date on which the Secretary determines that the alien was not an eligible individual under subsection (a)(2) as of the date that such conditional permanent resident status was granted, on which date of the Secretary\u2019s determination the alien shall no longer be an alien lawfully admitted for permanent residence; or\n**(3)**\nthe date on which the Secretary determines pursuant to subsection (c)(2) that the alien is not eligible for removal of conditions, on which date the alien shall no longer be an alien lawfully admitted for permanent residence.\n##### (e) Rule of construction\nNothing in this section shall be construed to limit the authority of the Secretary at any time to place in removal proceedings under section 240 of the Immigration and Nationality Act ( 8 U.S.C. 1229a ) any alien who has conditional permanent resident status under this section, if the alien is deportable under section 237 of such Act ( 8 U.S.C. 1227 ) under a ground of deportability applicable to an alien who has been lawfully admitted for permanent residence.\n##### (f) Parole expiration tolled\nThe expiration date of a period of parole shall not apply to an individual under consideration for conditional permanent resident status under this section, until such time as the Secretary has determined whether to issue conditional permanent resident status.\n##### (g) Periodic nonadversarial meetings\n**(1) In general**\nNot later than 180 days after the date on which an individual is conferred conditional permanent resident status under this section, and periodically thereafter, the Office of Refugee Resettlement shall make available opportunities for the individual to participate in a nonadversarial meeting, during which an official of the Office of Refugee Resettlement (or an agency funded by the Office) shall\u2014\n**(A)**\non request by the individual, assist the individual in a referral or application for applicable benefits administered by the Department of Health and Human Services and completing any applicable paperwork; and\n**(B)**\nanswer any questions regarding eligibility for other benefits administered by the United States Government.\n**(2) Notification of requirements**\nNot later than 7 days before the date on which a meeting under paragraph (1) is scheduled to occur, the Secretary of Health and Human Services shall provide notice to the individual that includes the date of the scheduled meeting and a description of the process for rescheduling the meeting.\n**(3) Conduct of meeting**\nThe Secretary of Health and Human Services shall implement practices to ensure that\u2014\n**(A)**\nmeetings under paragraph (1) are conducted in a nonadversarial manner; and\n**(B)**\ninterpretation and translation services are provided to individuals granted conditional permanent resident status under this section who have limited English proficiency.\n**(4) Rules of construction**\nNothing in this subsection shall be construed\u2014\n**(A)**\nto prevent an individual from electing to have counsel present during a meeting under paragraph (1); or\n**(B)**\nin the event that an individual declines to participate in such a meeting, to affect the individual's conditional permanent resident status under this section or eligibility to have conditions removed in accordance with this section.\n##### (h) Consideration\nExcept with respect to an application for naturalization and the benefits described in subsection (p), an individual in conditional permanent resident status under this section shall be considered to be an alien lawfully admitted for permanent residence for purposes of the adjudication of an application or petition for a benefit or the receipt of a benefit.\n##### (i) Notification of requirements\nNot later than 90 days after the date on which the status of an individual is adjusted to that of conditional permanent resident status under this section, the Secretary shall provide notice to such individual with respect to the provisions of this section, including subsection (c)(1) (relating to the conduct of assessments) and subsection (g) (relating to periodic nonadversarial meetings).\n##### (j) Application for naturalization\nThe Secretary shall establish procedures whereby an individual who would otherwise be eligible to apply for naturalization but for having conditional permanent resident status, may be considered for naturalization coincident with removal of conditions under subsection (c)(2).\n##### (k) Adjustment of status date\n**(1) In general**\nAn alien described in paragraph (2) shall be regarded as lawfully admitted for permanent residence as of the date the alien was initially inspected and admitted or paroled into the United States, or July 30, 2021, whichever is later.\n**(2) Alien described**\nAn alien described in this paragraph is an alien who\u2014\n**(A)**\nis described in subparagraph (A), (B), or (D) of subsection (a)(2), and whose status was adjusted to that of an alien lawfully admitted for permanent residence on or after July 30, 2021, but on or before the date of the enactment of this Act; or\n**(B)**\nis an eligible individual whose status is then adjusted to that of an alien lawfully admitted for permanent residence after the date of the enactment of this Act under any provision of the immigration laws other than this section.\n##### (l) Parents and legal guardians of unaccompanied children\nA parent or legal guardian of an eligible individual shall be eligible to obtain status as an alien lawfully admitted for permanent residence on a conditional basis if\u2014\n**(1)**\nthe eligible individual\u2014\n**(A)**\nwas under 18 years of age on the date on which the eligible individual was granted conditional permanent resident status under this section; and\n**(B)**\nwas not accompanied by at least one parent or guardian on the date the eligible individual was admitted or paroled into the United States; and\n**(2)**\nsuch parent or legal guardian was admitted or paroled into the United States after the date referred to in paragraph (1)(B).\n##### (m) Guidance\n**(1) Interim guidance**\n**(A) In general**\nNot later than 120 days after the date of the enactment of this Act, the Secretary shall issue guidance implementing this section.\n**(B) Publication**\nNotwithstanding section 553 of title 5, United States Code, guidance issued pursuant to subparagraph (A)\u2014\n**(i)**\nmay be published on the internet website of the Department of Homeland Security; and\n**(ii)**\nshall be effective on an interim basis immediately upon such publication but may be subject to change and revision after notice and an opportunity for public comment.\n**(2) Final guidance**\n**(A) In general**\nNot later than 180 days after the date of issuance of guidance under paragraph (1), the Secretary shall finalize the guidance implementing this section.\n**(B) Exemption from the Administrative Procedures Act**\nChapter 5 of title 5, United States Code (commonly known as the Administrative Procedures Act ), or any other law relating to rulemaking or information collection, shall not apply to the guidance issued under this paragraph.\n##### (n) Asylum claims\n**(1) In general**\nWith respect to the adjudication of an application for asylum submitted by an eligible individual, section 2502(c) of the Extending Government Funding and Delivering Emergency Assistance Act ( 8 U.S.C. 1101 note; Public Law 117\u201343 ) shall not apply.\n**(2) Rule of construction**\nNothing in this section may be construed to prohibit an eligible individual from seeking or receiving asylum under section 208 of the Immigration and Nationality Act ( 8 U.S.C. 1158 ).\n##### (o) Prohibition on fees\nThe Secretary may not charge a fee to any eligible individual in connection with the initial issuance under this section of\u2014\n**(1)**\na document evidencing status as an alien lawfully admitted for permanent residence or conditional permanent resident status; or\n**(2)**\nan employment authorization document.\n##### (p) Eligibility for benefits\n**(1) In general**\nNotwithstanding any other provision of law\u2014\n**(A)**\nan individual described in subsection (a) of section 2502 of the Afghanistan Supplemental Appropriations Act, 2022 ( 8 U.S.C. 1101 note; Public Law 117\u201343 ) shall retain his or her eligibility for the benefits and services described in subsection (b) of such section if the individual is under consideration for, or is granted, adjustment of status under this section; and\n**(B)**\nsuch benefits and services shall remain available to the individual to the same extent and for the same periods of time as such benefits and services are otherwise available to refugees who acquire such status.\n**(2) Exception from 5-year limited eligibility for means-tested public benefits**\nSection 403(b)(1) of the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 ( 8 U.S.C. 1613(b)(1) ) is amended by adding at the end the following:\n(F) An alien whose status is adjusted under section 4 of the Afghan Adjustment Act to that of an alien lawfully admitted for permanent residence or to that of an alien lawfully admitted for permanent residence on a conditional basis. .\n##### (q) Rule of construction\nNothing in this section may be construed to preclude an eligible individual from applying for or receiving any immigration benefit to which the individual is otherwise entitled.\n##### (r) Exemption from numerical limitations\n**(1) In general**\nAliens granted conditional permanent resident status or lawful permanent resident status under this section shall not be subject to the numerical limitations under sections 201, 202, and 203 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, and 1153).\n**(2) Spouse and children beneficiaries**\nA spouse or child who is the beneficiary of an immigrant petition under section 204 of the Immigration and Nationality Act ( 8 U.S.C. 1154 ) filed by an alien who has been granted conditional permanent resident status or lawful permanent resident status under this section, seeking classification of the spouse or child under section 203(a)(2)(A) of that Act ( 8 U.S.C. 1153(a)(2)(A) ) shall not be subject to the numerical limitations under sections 201, 202, and 203 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, and 1153).\n##### (s) Effect on other applications\nNotwithstanding any other provision of law, in the interest of efficiency, the Secretary may pause consideration of any application or request for an immigration benefit pending adjudication so as to prioritize consideration of adjustment of status to an alien lawfully admitted for permanent residence on a conditional basis under this section.\n##### (t) Authorization for appropriations\nThere is authorized to be appropriated to the Attorney General, the Secretary of Health and Human Services, the Secretary, and the Secretary of State such sums as are necessary to carry out this section.\n#### 5. Refugee processes for certain at-risk Afghan allies\n##### (a) Definition of Afghan ally\n**(1) In general**\nIn this section, the term Afghan ally means an alien who is a citizen or national of Afghanistan, or in the case of an alien having no nationality, an alien who last habitually resided in Afghanistan, who\u2014\n**(A)**\nwas\u2014\n**(i)**\na member of\u2014\n**(I)**\nthe special operations forces of the Afghanistan National Defense and Security Forces;\n**(II)**\nthe Afghanistan National Army Special Operations Command;\n**(III)**\nthe Afghan Air Force; or\n**(IV)**\nthe Special Mission Wing of Afghanistan;\n**(ii)**\na female member of any other entity of the Afghanistan National Defense and Security Forces, including\u2014\n**(I)**\na cadet or instructor at the Afghanistan National Defense University; and\n**(II)**\na civilian employee of the Ministry of Defense or the Ministry of Interior Affairs;\n**(iii)**\nan individual associated with former Afghan military and police human intelligence activities, including operators and Department of Defense sources;\n**(iv)**\nan individual associated with former Afghan military counterintelligence, counterterrorism, or counternarcotics;\n**(v)**\nan individual associated with the former Afghan Ministry of Defense, Ministry of Interior Affairs, or court system, and who was involved in the investigation, prosecution or detention of combatants or members of the Taliban or criminal networks affiliated with the Taliban;\n**(vi)**\nan individual employed in the former justice sector in Afghanistan as a judge, prosecutor, or investigator who was engaged in rule of law activities for which the United States provided funding or training; or\n**(vii)**\na senior military officer, senior enlisted personnel, or civilian official who served on the staff of the former Ministry of Defense or the former Ministry of Interior Affairs of Afghanistan; or\n**(B)**\nprovided service to an entity or organization described in subparagraph (A) for not less than 1 year during the period beginning on December 22, 2001, and ending on September 1, 2021, and did so in support of the United States mission in Afghanistan.\n**(2) Inclusions**\nFor purposes of this section, the Afghanistan National Defense and Security Forces includes members of the security forces under the Ministry of Defense and the Ministry of Interior Affairs of the Islamic Republic of Afghanistan, including the Afghanistan National Army, the Afghan Air Force, the Afghanistan National Police, and any other entity designated by the Secretary of Defense as part of the Afghanistan National Defense and Security Forces during the relevant period of service of the applicant concerned.\n##### (b) Refugee status for Afghan allies\n**(1) Designation as refugees of special humanitarian concern**\nAfghan allies shall be considered refugees of special humanitarian concern under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ), until the later of 10 years after the date of enactment of this Act or upon determination by the Secretary of State, in consultation with the Secretary of Defense and the Secretary, that such designation is no longer in the interest of the United States.\n**(2) Third country presence not required**\nNotwithstanding section 101(a)(42) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(42) ), the Secretary of State and the Secretary shall, to the greatest extent possible, conduct remote refugee processing for an Afghan ally located in Afghanistan.\n##### (c) Afghan allies referral program\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act\u2014\n**(A)**\nthe Secretary of Defense, in consultation with the Secretary of State, shall establish a process by which an individual may apply to the Secretary of Defense for classification as an Afghan ally and request a referral to the United States Refugee Admissions Program; and\n**(B)**\nthe head of any appropriate department or agency that conducted operations in Afghanistan during the period beginning on December 22, 2001, and ending on September 1, 2021, in consultation with the Secretary of State, may establish a process by which an individual may apply to the head of the appropriate department or agency for classification as an Afghan ally and request a referral to the United States Refugee Admissions Program.\n**(2) Application system**\n**(A) In general**\nThe process established under paragraph (1) shall\u2014\n**(i)**\ninclude the development and maintenance of a secure online portal through which applicants may provide information verifying their status as Afghan allies and upload supporting documentation; and\n**(ii)**\nallow\u2014\n**(I)**\nan applicant to submit his or her own application;\n**(II)**\na designee of an applicant to submit an application on behalf of the applicant; and\n**(III)**\nin the case of an applicant who is outside the United States, the submission of an application regardless of where the applicant is located.\n**(B) Use by other agencies**\nThe Secretary of Defense\u2014\n**(i)**\nmay enter into arrangements with the head of any other appropriate department or agency so as to allow the application system established under subparagraph (A) to be used by such department or agency; and\n**(ii)**\nshall notify the Secretary of State of any such arrangement.\n**(3) Review process**\nAs soon as practicable after receiving a request for classification and referral described in paragraph (1), the head of the appropriate department or agency shall\u2014\n**(A)**\nreview\u2014\n**(i)**\nthe service record of the applicant, if available;\n**(ii)**\nif the applicant provides a service record or other supporting documentation, any information that helps verify the service record concerned, including information or an attestation provided by any current or former official of the department or agency who has personal knowledge of the eligibility of the applicant for such classification and referral; and\n**(iii)**\nthe data holdings of the department or agency and other cooperating interagency partners, including as applicable biographic and biometric records, iris scans, fingerprints, voice biometric information, hand geometry biometrics, other identifiable information, and any other information related to the applicant, including relevant derogatory information; and\n**(B)**\n**(i)**\nin a case in which the head of the department or agency determines that the applicant is an Afghan ally without significant derogatory information, refer the Afghan ally to the United States Refugee Admissions Program as a refugee; and\n**(ii)**\ninclude with such referral\u2014\n**(I)**\nany service record concerned, if available;\n**(II)**\nif the applicant provides a service record, any information that helps verify the service record concerned; and\n**(III)**\nany biometrics for the applicant.\n**(4) Review process for denial of request for referral**\n**(A) In general**\nIn the case of an applicant with respect to whom the head of the appropriate department or agency denies a request for classification and referral based on a determination that the applicant is not an Afghan ally or based on derogatory information\u2014\n**(i)**\nthe head of the department or agency shall provide the applicant with a written notice of the denial that provides, to the maximum extent practicable, a description of the basis for the denial, including the facts and inferences, or evidentiary gaps, underlying the individual determination; and\n**(ii)**\nthe applicant shall be provided an opportunity to submit not more than 1 written appeal to the head of the department or agency for each such denial.\n**(B) Deadline for appeal**\nAn appeal under clause (ii) of subparagraph (A) shall be submitted\u2014\n**(i)**\nnot more than 120 days after the date on which the applicant concerned receives notice under clause (i) of that subparagraph; or\n**(ii)**\non any date thereafter, at the discretion of the head of the appropriate department or agency.\n**(C) Request to reopen**\n**(i) In general**\nAn applicant who receives a denial under subparagraph (A) may submit a request to reopen a request for classification and referral under the process established under paragraph (1) so that the applicant may provide additional information, clarify existing information, or explain any unfavorable information.\n**(ii) Limitation**\nAfter considering 1 such request to reopen from an applicant, the head of the appropriate department or agency may deny subsequent requests to reopen submitted by the same applicant.\n**(5) Form and content of referral**\nTo the extent practicable, the head of the appropriate department or agency shall ensure that referrals made under this subsection\u2014\n**(A)**\nconform to requirements established by the Secretary of State for form and content; and\n**(B)**\nare complete and include sufficient contact information, supporting documentation, and any other material the Secretary of State or the Secretary consider necessary or helpful in determining whether an applicant is entitled to refugee status.\n**(6) Termination**\nThe application process and referral system under this subsection shall terminate upon the later of 1 year before the termination of the designation under subsection (b)(1) or on the date of a joint determination by the Secretary of State and the Secretary of Defense, in consultation with the Secretary, that such termination is in the national interest of the United States.\n##### (d) General provisions\n**(1) Prohibition on fees**\nThe Secretary, the Secretary of Defense, the Secretary of State, or the head of any appropriate department or agency referring Afghan allies under this section may not charge any fee in connection with a request for a classification and referral as a refugee under this section.\n**(2) Defense personnel**\nAny limitation in law with respect to the number of personnel within the Office of the Secretary of Defense, the military departments, or a Defense Agency (as defined in section 101(a) of title 10, United States Code) shall not apply to personnel employed for the primary purpose of carrying out this section.\n**(3) Representation**\nAn alien applying for admission to the United States under this section may be represented during the application process, including at relevant interviews and examinations, by an attorney or other accredited representative. Such representation shall not be at the expense of the United States Government.\n**(4) Protection of aliens**\nThe Secretary of State, in consultation with the head of any other appropriate Federal agency, shall make a reasonable effort to provide an alien who has been classified as an Afghan ally and has been referred as a refugee under this section protection or to immediately remove such alien from Afghanistan, if possible.\n**(5) Other eligibility for immigrant status**\nNo alien shall be denied the opportunity to apply for admission under this section solely because the alien qualifies as an immediate relative or is eligible for any other immigrant classification.\n**(6) Authorization of appropriations**\nThere are authorized to be appropriated such sums as necessary for each of fiscal years 2025 through 2034 to carry out this section.\n##### (e) Rule of construction\nNothing in this section may be construed to inhibit the Secretary of State from accepting refugee referrals from any entity.\n#### 6. Improving efficiency and oversight of refugee and special immigrant processing\n##### (a) Acceptance of fingerprint cards and submissions of biometrics\nIn addition to the methods authorized under the heading relating to the Immigration and Naturalization Service under title I of the Departments of Commerce, Justice, and State, the Judiciary, and Related Agencies Appropriations Act of 1998 ( Public Law 105\u2013119 , 111 Stat. 2448; 8 U.S.C. 1103 note), and other applicable law, and subject to such safeguards as the Secretary, in consultation with the Secretary of State or the Secretary of Defense, as appropriate, shall prescribe to ensure the integrity of the biometric collection (which shall include verification of identity by comparison of such fingerprints with fingerprints taken by or under the direct supervision of the Secretary prior to or at the time of the individual\u2019s application for admission to the United States), the Secretary may, in the case of any application for any benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ), accept fingerprint cards or any other submission of biometrics\u2014\n**(1)**\nprepared by international or nongovernmental organizations under an appropriate agreement with the Secretary or the Secretary of State;\n**(2)**\nprepared by employees or contractors of the Department of Homeland Security or the Department of State; or\n**(3)**\nprovided by an agency (as defined under section 3502 of title 44, United States Code).\n##### (b) Staffing\n**(1) Vetting**\nThe Secretary of State, the Secretary, the Secretary of Defense, and any other agency authorized to carry out the vetting process under this Act, shall each ensure sufficient staffing, and request the resources necessary, to efficiently and adequately carry out the vetting of applicants for\u2014\n**(A)**\nreferral to the United States Refugee Admissions Program, consistent with the determinations established under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ); and\n**(B)**\nspecial immigrant status.\n**(2) Refugee resettlement**\nThe Secretary of Health and Human Services shall ensure sufficient staffing to efficiently provide assistance under chapter 2 of title IV of the Immigration and Nationality Act ( 8 U.S.C. 1521 et seq. ) to refugees resettled in the United States.\n##### (c) Remote processing\nNotwithstanding any other provision of law, the Secretary of State and the Secretary shall employ remote processing capabilities for refugee processing under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ), including secure digital file transfers, videoconferencing and teleconferencing capabilities, remote review of applications, remote interviews, remote collection of signatures, waiver of the applicant\u2019s appearance or signature (other than a final appearance and verification by the oath of the applicant prior to or at the time of the individual\u2019s application for admission to the United States), waiver of signature for individuals under 5 years old, and any other capability the Secretary of State and the Secretary consider appropriate, secure, and likely to reduce processing wait times at particular facilities.\n##### (d) Monthly arrival reports\nWith respect to monthly reports issued by the Secretary of State relating to United States Refugee Admissions Program arrivals, the Secretary of State shall report\u2014\n**(1)**\nthe number of monthly admissions of refugees, disaggregated by priorities; and\n**(2)**\nthe number of Afghan allies admitted as refugees.\n##### (e) Interagency Task Force on Afghan Ally Strategy\n**(1) Establishment**\nNot later than 180 days after the date of the enactment of this Act, the President shall establish an Interagency Task Force on Afghan Ally Strategy (referred to in this section as the Task Force )\u2014\n**(A)**\nto develop and oversee the implementation of the strategy and contingency plan described in subparagraph (A)(i) of paragraph (4); and\n**(B)**\nto submit the report, and provide a briefing on the report, as described in subparagraphs (A) and (B) of paragraph (4).\n**(2) Membership**\n**(A) In general**\nThe Task Force shall include\u2014\n**(i)**\n1 or more representatives from each relevant Federal agency, as designated by the head of the applicable relevant Federal agency; and\n**(ii)**\nany other Federal Government official designated by the President.\n**(B) Relevant Federal agency defined**\nIn this paragraph, the term relevant Federal agency means\u2014\n**(i)**\nthe Department of State;\n**(ii)**\nthe Department of Homeland Security;\n**(iii)**\nthe Department of Defense;\n**(iv)**\nthe Department of Health and Human Services;\n**(v)**\nthe Department of Justice; and\n**(vi)**\nthe Office of the Director of National Intelligence.\n**(3) Chair**\nThe Task Force shall be chaired by the Secretary of State.\n**(4) Duties**\n**(A) Report**\n**(i) In general**\nNot later than 180 days after the date on which the Task Force is established, the Task Force, acting through the chair of the Task Force, shall submit a report to the appropriate committees of Congress that includes\u2014\n**(I)**\na strategy for facilitating the resettlement of nationals of Afghanistan outside the United States who, during the period beginning on October 1, 2001, and ending on September 1, 2021, directly and personally supported the United States mission in Afghanistan, as determined by the Secretary of State in consultation with the Secretary of Defense; and\n**(II)**\na contingency plan for future emergency operations in foreign countries involving foreign nationals who have worked directly with the United States Government, including the Armed Forces of the United States and United States intelligence agencies.\n**(ii) Elements**\nThe report required under clause (i) shall include\u2014\n**(I)**\nthe total number of nationals of Afghanistan who have pending specified applications, disaggregated by\u2014\n**(aa)**\nsuch nationals in Afghanistan and such nationals in a third country;\n**(bb)**\ntype of specified application; and\n**(cc)**\napplications that are documentarily complete and applications that are not documentarily complete;\n**(II)**\nan estimate of the number of nationals of Afghanistan who may be eligible for special immigrant status or classification as an Afghan ally;\n**(III)**\nwith respect to the strategy required under subparagraph (A)(i)(I)\u2014\n**(aa)**\nthe estimated number of nationals of Afghanistan described in such subparagraph;\n**(bb)**\na description of the process for safely resettling such nationals of Afghanistan;\n**(cc)**\na plan for processing such nationals of Afghanistan for admission to the United States that\u2014\n(AA)\ndiscusses the feasibility of remote processing for such nationals of Afghanistan residing in Afghanistan;\n(BB)\nincludes any strategy for facilitating refugee and consular processing for such nationals of Afghanistan in third countries, and the timelines for such processing;\n(CC)\nincludes a plan for conducting rigorous and efficient vetting of all such nationals of Afghanistan for processing;\n(DD)\ndiscusses the availability and capacity of sites in third countries to process applications and conduct any required vetting for such nationals of Afghanistan, including the potential to establish additional sites; and\n(EE)\nincludes a plan for providing updates and necessary information to affected individuals and relevant nongovernmental organizations;\n**(dd)**\na description of considerations, including resource constraints, security concerns, missing or inaccurate information, and diplomatic considerations, that limit the ability of the Secretary of State or the Secretary to increase the number of such nationals of Afghanistan who can be safely processed or resettled;\n**(ee)**\nan identification of any resource or additional authority necessary to increase the number of such nationals of Afghanistan who can be processed or resettled;\n**(ff)**\nan estimate of the cost to fully implement the strategy; and\n**(gg)**\nany other matter the Task Force considers relevant to the implementation of the strategy;\n**(IV)**\nwith respect to the contingency plan required by clause (i)(II)\u2014\n**(aa)**\na description of the standard practices for screening and vetting foreign nationals considered to be eligible for resettlement in the United States, including a strategy for vetting, and maintaining the records of, such foreign nationals who are unable to provide identification documents or biographic details due to emergency circumstances;\n**(bb)**\na strategy for facilitating refugee or consular processing for such foreign nationals in third countries;\n**(cc)**\nclear guidance with respect to which Federal agency has the authority and responsibility to coordinate Federal resettlement efforts;\n**(dd)**\na description of any resource or additional authority necessary to coordinate Federal resettlement efforts, including the need for a contingency fund; and\n**(ee)**\nany other matter the Task Force considers relevant to the implementation of the contingency plan; and\n**(V)**\na strategy for the efficient processing of all Afghan special immigrant visa applications and appeals, including\u2014\n**(aa)**\na review of current staffing levels and needs across all interagency offices and officials engaged in the special immigrant visa process;\n**(bb)**\nan analysis of the expected Chief of Mission approvals and denials of applications in the pipeline in order to project the expected number of visas necessary to provide special immigrant status to all approved applicants under this Act during the several years after the date of the enactment of this Act;\n**(cc)**\nan assessment as to whether adequate guidelines exist for reconsidering or reopening applications for special immigrant visas in appropriate circumstances and consistent with applicable laws; and\n**(dd)**\nan assessment of the procedures throughout the special immigrant visa application process, including at the Portsmouth Consular Center, and the effectiveness of communication between the Portsmouth Consular Center and applicants, including an identification of any area in which improvements to the efficiency of such procedures and communication may be made.\n**(iii) Form**\nThe report required under clause (i) shall be submitted in unclassified form but may include a classified annex.\n**(B) Briefing**\nNot later than 60 days after submitting the report required by clause (i), the Task Force shall brief the appropriate committees of Congress on the contents of the report.\n**(5) Termination**\nThe Task Force shall remain in effect until the later of\u2014\n**(A)**\nthe date on which the strategy required under paragraph (4)(A)(i)(I) has been fully implemented;\n**(B)**\nthe date of a determination by the Secretary of State, in consultation with the Secretary of Defense and the Secretary, that a task force is no longer necessary for the implementation of subparagraphs (A) and (B) of paragraph (1); or\n**(C)**\nthe date that is 10 years after the date of the enactment of this Act.\n##### (f) Improving consultation with Congress\nSection 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) is amended\u2014\n**(1)**\nin subsection (a), by amending paragraph (4) to read as follows:\n(4) (A) In the determination made under this subsection for each fiscal year (beginning with fiscal year 1992), the President shall enumerate, with the respective number of refugees so determined, the number of aliens who were granted asylum in the previous year. (B) In making a determination under paragraph (1), the President shall consider the information in the most recently published projected global resettlement needs report published by the United Nations High Commissioner for Refugees. ;\n**(2)**\nin subsection (e), by amending paragraph (2) to read as follows:\n(2) A description of the number and allocation of the refugees to be admitted, including the expected allocation by region, and an analysis of the conditions within the countries from which they came. ; and\n**(3)**\nby adding at the end the following\u2014\n(g) Quarterly reports on admissions Not later than 30 days after the last day of each quarter beginning the fourth quarter of fiscal year 2025, the President shall submit to the Committee on Homeland Security and Governmental Affairs, the Committee on the Judiciary, and the Committee on Foreign Relations of the Senate and the Committee on Homeland Security, the Committee on the Judiciary, and the Committee on Foreign Affairs of the House of Representatives a report that includes the following: (1) Refugees admitted (A) The number of refugees admitted to the United States during the preceding quarter. (B) The cumulative number of refugees admitted to the United States during the applicable fiscal year, as of the last day of the preceding quarter. (C) The number of refugees expected to be admitted to the United States during the remainder of the applicable fiscal year. (D) The number of refugees from each region admitted to the United States during the preceding quarter. (2) Refugee applicants with pending security checks (A) The number of aliens, by nationality, security check, and responsible vetting agency, for whom a National Vetting Center or other security check has been requested during the preceding quarter, and the number of aliens, by nationality, for whom the check was pending beyond 30 days. (B) The number of aliens, by nationality, security check, and responsible vetting agency, for whom a National Vetting Center or other security check has been pending for more than 180 days. (3) Circuit rides (A) For the preceding quarter\u2014 (i) the number of Refugee Corps officers deployed on circuit rides and the overall number of Refugee Corps officers; (ii) the number of individuals interviewed\u2014 (I) on each circuit ride; and (II) at each circuit ride location; (iii) the number of circuit rides; and (iv) for each circuit ride, the duration of the circuit ride. (B) For the subsequent 2 quarters\u2014 (i) the number of circuit rides planned; and (ii) the number of individuals planned to be interviewed. (4) Processing (A) For refugees admitted to the United States during the preceding quarter, the average number of days between\u2014 (i) the date on which an individual referred to the United States Government as a refugee applicant is interviewed by the Secretary of Homeland Security; and (ii) the date on which such individual is admitted to the United States. (B) For refugee applicants interviewed by the Secretary of Homeland Security in the preceding quarter, the approval, denial, recommended approval, recommended denial, and hold rates for the applications for admission of such individuals, disaggregated by nationality. .\n#### 7. Support for certain vulnerable Afghans relating to employment by or on behalf of the United States\n##### (a) Special immigrant visas for certain relatives of certain members of the Armed Forces\n**(1) In general**\nSection 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ) is amended\u2014\n**(A)**\nin subparagraph (L)(iii), by adding a semicolon at the end;\n**(B)**\nin subparagraph (M), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(N) a citizen or national of Afghanistan who is the parent or brother or sister of\u2014 (i) a member of the Armed Forces (as defined in section 101(a) of title 10, United States Code); or (ii) a veteran (as defined in section 101 of title 38, United States Code). .\n**(2) Numerical limitations**\n**(A) In general**\nSubject to subparagraph (C), the total number of principal aliens who may be provided special immigrant visas under subparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ), as added by paragraph (1), may not exceed 2,500 each fiscal year.\n**(B) Carryover**\nIf the numerical limitation specified in subparagraph (A) is not reached during a given fiscal year, the numerical limitation specified in such subparagraph for the following fiscal year shall be increased by a number equal to the difference between\u2014\n**(i)**\nthe numerical limitation specified in subparagraph (A) for the given fiscal year; and\n**(ii)**\nthe number of principal aliens provided special immigrant visas under subparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ) during the given fiscal year.\n**(C) Maximum number of visas**\nThe total number of aliens who may be provided special immigrant visas under subparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ) shall not exceed 10,000.\n**(D) Duration of authority**\nThe authority to issue visas under subparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ) shall\u2014\n**(i)**\ncommence on the date of the enactment of this Act; and\n**(ii)**\nterminate on the date on which all such visas are exhausted.\n##### (b) Certain Afghans injured or killed in the course of employment\nSection 602(b) of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note; Public Law 111\u20138 ) is amended\u2014\n**(1)**\nin paragraph (2)(A)\u2014\n**(A)**\nby amending clause (ii) to read as follows:\n(ii) (I) was or is employed in Afghanistan on or after October 7, 2001, for not less than 1 year\u2014 (aa) by, or on behalf of, the United States Government; or (bb) by the International Security Assistance Force (or any successor name for such Force) in a capacity that required the alien\u2014 (AA) while traveling off-base with United States military personnel stationed at the International Security Assistance Force (or any successor name for such Force), to serve as an interpreter or translator for such United States military personnel; or (BB) to perform activities for the United States military personnel stationed at International Security Assistance Force (or any successor name for such Force); or (II) in the case of an alien who was wounded or seriously injured in connection with employment described in subclause (I), was employed for any period until the date on which such wound or injury occurred, if the wound or injury prevented the alien from continuing such employment; ; and\n**(B)**\nin clause (iii), by striking clause (ii) and inserting clause (ii)(I) ;\n**(2)**\nin paragraph (13)(A)(i), by striking subclause (I) or (II)(bb) of paragraph (2)(A)(ii) and inserting item (aa) or (bb)(BB) of paragraph (2)(A)(ii)(I) ;\n**(3)**\nin paragraph (14)(C), by striking paragraph (2)(A)(ii) and inserting paragraph (2)(A)(ii)(I) ; and\n**(4)**\nin paragraph (15), by striking paragraph (2)(A)(ii) and inserting paragraph (2)(A)(ii)(I) .\n##### (c) Extension of special immigrant visa program under Afghan Allies Protection Act of 2009\nSection 602(b) of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note; Public Law 111\u20138 ) is amended\u2014\n**(1)**\nin paragraph (3)(F)\u2014\n**(A)**\nin the subparagraph heading, by striking Fiscal years 2015 through 2022 and inserting Fiscal years 2015 through 2029 ;\n**(B)**\nin clause (i), by striking December 31, 2024 and inserting December 31, 2029 ; and\n**(C)**\nin clause (ii), by striking December 31, 2024 and inserting December 31, 2029 ; and\n**(2)**\nin paragraph (13), in the matter preceding subparagraph (A), by striking January 31, 2024 and inserting January 31, 2030 .\n##### (d) Authorization of virtual interviews\nSection 602(b)(4) of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note; Public Law 111\u20138 ;) is amended by adding at the end the following:\n(D) Virtual interviews Notwithstanding section 222(e) of the Immigration and Nationality Act ( 8 U.S.C. 1202(e) ), an application for an immigrant visa under this section may be signed by the applicant through a virtual video meeting before a consular officer and verified by the oath of the applicant administered by the consular officer during a virtual video meeting. .\n##### (e) Quarterly reports\nParagraph (12) of section 602(b) of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note; Public Law 111\u20138 ) is amended is amended to read as follows:\n(12) Quarterly reports (A) Report to Congress Not later than 120 days after the date of enactment of the Afghan Adjustment Act and every 90 days thereafter, the Secretary of State and the Secretary of Homeland Security, in consultation with the Secretary of Defense, shall submit to the appropriate committees of Congress a report that includes the following: (i) For the preceding quarter\u2014 (I) a description of improvements made to the processing of special immigrant visas and refugee processing for citizens and nationals of Afghanistan; (II) the number of new Afghan referrals to the United States Refugee Admissions Program, disaggregated by referring entity; (III) the number of interviews of Afghans conducted by U.S. Citizenship and Immigration Services, disaggregated by the country in which such interviews took place; (IV) the number of approvals and the number of denials of refugee status requests for Afghans; (V) the number of total admissions to the United States of Afghan refugees; (VI) number of such admissions, disaggregated by whether the refugees come from within, or outside of, Afghanistan; (VII) the average processing time for citizens and nationals of Afghanistan who are applicants; (VIII) the number of such cases processed within such average processing time; and (IX) the number of denials issued with respect to applications by citizens and nationals of Afghanistan. (ii) The number of applications by citizens and nationals of Afghanistan for refugee referrals pending as of the date of submission of the report. (iii) A description of the efficiency improvements made in the process by which applications for special immigrant visas under this subsection are processed, including information described in clauses (iii) through (viii) of paragraph (11)(B). (B) Form of report Each report required by subparagraph (A) shall be submitted in unclassified form but may contain a classified annex. (C) Public posting The Secretary of State shall publish on the website of the Department of State the unclassified portion of each report submitted under subparagraph (A). .\n##### (f) General provisions\n**(1) Prohibition on fees**\nThe Secretary, the Secretary of Defense, or the Secretary of State may not charge any fee in connection with an application for, or issuance of, a special immigrant visa or special immigrant status under\u2014\n**(A)**\nsection 602 of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note; Public Law 111\u20138 );\n**(B)**\nsection 1059 of the National Defense Authorization Act for Fiscal Year 2006 ( 8 U.S.C. 1101 note; Public Law 109\u2013163 ); or\n**(C)**\nsubparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ), as added by subsection (a)(1).\n**(2) Defense personnel**\nAny limitation in law with respect to the number of personnel within the Office of the Secretary of Defense, the military departments, or a Defense Agency (as defined in section 101(a) of title 10, United States Code) shall not apply to personnel employed for the primary purpose of carrying out this section.\n**(3) Protection of aliens**\nThe Secretary of State, in consultation with the head of any other appropriate Federal agency, shall make a reasonable effort to provide an alien who is seeking status as a special immigrant under subparagraph (N) of section 101(a)(27) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27) ), as added by subsection (a)(1), protection or to immediately remove such alien from Afghanistan, if possible.\n**(4) Resettlement support**\nA citizen or national of Afghanistan who is admitted to the United States under this section or an amendment made by this section shall be eligible for resettlement assistance, entitlement programs, and other benefits available to refugees admitted under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) to the same extent, and for the same periods of time, as such refugees.\n#### 8. Support for allies seeking resettlement in the United States\nNotwithstanding any other provision of law, during the period beginning on the date of the enactment of this Act and ending on the date that is 10 years thereafter, the Secretary and the Secretary of State may waive any fee or surcharge or exempt individuals from the payment of any fee or surcharge collected by the Department of Homeland Security and the Department of State, respectively, in connection with a petition or application for, or issuance of, an immigrant visa to a national of Afghanistan under section 201(b)(2)(A)(i) or 203(a) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(2)(A)(i) and 1153(a)), respectively.\n#### 9. Reporting\n##### (a) Quarterly reports\nBeginning on January 1, 2028, not less frequently than quarterly, the Secretary shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes, for the preceding quarter\u2014\n**(1)**\nthe number of individuals granted conditional permanent resident status under section 4, disaggregated by the number of such individuals for whom conditions have been removed;\n**(2)**\nthe number of individuals granted conditional permanent resident status under section 4 who have been determined to be ineligible for removal of conditions (and the reasons for such determination); and\n**(3)**\nthe number of individuals granted conditional permanent resident status under section 4 for whom no such determination has been made (and the reasons for the lack of such determination).\n##### (b) Annual reports\nNot less frequently than annually, the Secretary, in consultation with the Attorney General, shall submit to the appropriate committees of Congress a report that includes for the preceding year, with respect to individuals granted conditional permanent resident status under section 4\u2014\n**(1)**\nthe number of such individuals who are placed in removal proceedings under section 240 of the Immigration and Nationality Act ( 8 U.S.C. 1229a ) charged with a ground of deportability under subsection (a)(2) of section 237 of that Act ( 8 U.S.C. 1227 ), disaggregated by each applicable ground under that subsection;\n**(2)**\nthe number of such individuals who are placed in removal proceedings under section 240 of the Immigration and Nationality Act ( 8 U.S.C. 1229a ) charged with a ground of deportability under subsection (a)(3) of section 237 of that Act ( 8 U.S.C. 1227 ), disaggregated by each applicable ground under that subsection;\n**(3)**\nthe number of final orders of removal issued pursuant to proceedings described in paragraphs (1) and (2), disaggregated by each applicable ground of deportability;\n**(4)**\nthe number of such individuals for whom such proceedings are pending, disaggregated by each applicable ground of deportability; and\n**(5)**\na review of the available options for removal from the United States, including any changes in the feasibility of such options during the preceding year.\n#### 10. Rule of construction\nExcept as expressly described in this Act or an amendment made by this Act, nothing in this Act or an amendment made by this Act may be construed to modify, expand, or limit any law or authority to process or admit refugees under section 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) or applicants for an immigrant visa under the immigration laws.",
      "versionDate": "2025-08-05",
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
        "actionDate": "2025-08-01",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2679",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fulfilling Promises to Afghan Allies Act",
      "type": "S"
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
        "updateDate": "2025-09-18T19:51:12Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4895ih.xml"
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
      "title": "Afghan Adjustment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Afghan Adjustment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act and the Afghan Allies Protection Act of 2009, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:30Z"
    }
  ]
}
```
