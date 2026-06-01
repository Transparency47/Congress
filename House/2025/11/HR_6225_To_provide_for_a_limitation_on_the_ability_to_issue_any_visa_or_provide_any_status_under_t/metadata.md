# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6225?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6225
- Title: PAUSE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6225
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-05-08T08:06:52Z
- Update date including text: 2026-05-08T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6225",
    "number": "6225",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "PAUSE Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:52Z",
    "updateDateIncludingText": "2026-05-08T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:00:25Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TN"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "CO"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "AZ"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "FL"
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
      "sponsorshipDate": "2025-12-12",
      "state": "TX"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TN"
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
      "sponsorshipDate": "2026-01-30",
      "state": "AZ"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "OK"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
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
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6225ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6225\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Roy (for himself, Mr. Biggs of Arizona , Mr. Self , Mr. Ogles , Ms. Boebert , Mr. Gill of Texas , Mr. Fine , and Mr. Crane ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for a limitation on the ability to issue any visa or provide any status under the immigration laws until certain conditions have been met.\n#### 1. Short title\nThis Act may be cited as the Pausing on Admissions Until Security Ensured Act of 2025 or as the PAUSE Act of 2025 .\n#### 2. Limitation\n##### (a) In general\nNotwithstanding any other provision of law, but except as provided in subsection (c), no alien may be issued a visa or provided any status under the immigration laws, until the immigration laws provide that\u2014\n**(1)**\nStates and localities are not prohibited from denying access to public schools to aliens present in the United States without lawful status under the immigration laws;\n**(2)**\nno nonimmigrant may adjust status to that of an alien lawfully admitted for permanent residence;\n**(3)**\ncitizenship at birth is only available to a child who\u2014\n**(A)**\nis born in the United States; and\n**(B)**\nhas at least one parent who is\u2014\n**(i)**\na citizen of the United States; or\n**(ii)**\nan alien lawfully admitted for permanent residency in the United States;\n**(4)**\nno alien may be accorded any status under section 201(a)(1) of the Immigration and Nationality Act unless that alien is\u2014\n**(A)**\nthe spouse or minor child of a United States citizen; or\n**(B)**\nthe spouse or minor child of an alien lawfully admitted for permanent residency;\n**(5)**\nno alien may be accorded any lawful status under the immigration laws if that alien is\u2014\n**(A)**\nan Islamist;\n**(B)**\nan observer of Sharia law;\n**(C)**\na member or associate of the Chinese Communist Party;\n**(D)**\na known or suspected terrorist;\n**(E)**\na known or suspected member of a foreign terrorist organization; or\n**(F)**\na person who is affiliated with any foreign terrorist organization; and\n**(6)**\nno alien may be provided\u2014\n**(A)**\nany benefit payable under title XVIII of the Social Security Act (relating to the medicare program);\n**(B)**\nmedical assistance under title XIX of the Social Security Act (or any successor program to such title) for care and services that are necessary for the treatment of an emergency medical condition (as defined in section 1903(v)(3) of such Act) of the alien involved and are not related to an organ transplant procedure, if the alien involved otherwise meets the eligibility requirements for medical assistance under the State plan approved under such title (other than the requirement of the receipt of aid or assistance under title IV of such Act, supplemental security income benefits under title XVI of such Act, or a State supplementary payment);\n**(C)**\nany benefit under the supplemental security income program under title XVI of the Social Security Act, including supplementary payments pursuant to an agreement for Federal administration under section 1616(a) of the Social Security Act and payments pursuant to an agreement entered into under section 212(b) of Public Law 93\u201366 ;\n**(D)**\nany benefit under the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. );\n**(E)**\nany credit under section 36B of the Internal Revenue Code of 1986;\n**(F)**\nany credit under section 32 of the Internal Revenue Code of 1986;\n**(G)**\nany benefit under the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 );\n**(H)**\na loan made, insured, or guaranteed under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. );\n**(I)**\nany benefit under any program for housing or community development assistance or financial assistance administered by the Secretary of Housing and Urban Development, any program under title V of the Housing Act of 1949, or any assistance under section 306C of the Consolidated Farm and Rural Development Act; and\n**(J)**\nany loan or loan guarantee under the Small Business Act.\n##### (b) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall take effect on the date of the enactment of this Act.\n**(2) Prior application**\nNotwithstanding paragraph (1), in the case of any alien who applied for any status under the immigration laws before the date of the enactment of this Act who is ineligible for such status by reason of the enactment of this Act, such application shall be revoked, and any fee paid by such alien shall be refunded.\n##### (c) Exception\nThe prohibition on the issuance of a visa or provision of status under subsection (a) does not apply in the case of a visa or status under section 101(a)(15)(B)(ii).\n#### 3. H-1B fees\nSection 214(c) of the Immigration and Nationality Act ( 8 U.S.C. 1184(c) ) is amended by adding at the end the following:\n(D) Additional fee Notwithstanding any other provision of law, beginning with fiscal year 2026, a fee of $100,000 shall be imposed on an employer filing a petition under paragraph (1)\u2014 (i) initially to grant an alien nonimmigrant status described in section 101(a)(15)(H)(i)(b); (ii) to extend the stay of an alien having such status (unless the employer previously has obtained an extension for such alien); or (iii) to obtain authorization for an alien having such status to change employers. .\n#### 4. Termination of the Optional Practical Training Program\n##### (a) Eliminating the optional practical training program\nSection 274A(h) of the Immigration and Nationality Act ( 8 U.S.C. 1324a ) is amended by adding at the end the following:\n(4) Employment authorization for aliens no longer engaged in full-time study in the united states Notwithstanding any other provision of law, no alien present in the United States as a nonimmigrant under section 101(a)(15)(F)(i) may be provided employment authorization in the United States. .\n##### (b) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall take effect on the date of the enactment of this Act.\n**(2) Selectees**\nNotwithstanding paragraph (1), in the case of any alien who registered for the Optional Practical Training Program and received notification before the date of the enactment of this Act that he or she has been selected for employment authorization pursuant to such program, such authorization shall be revoked, and any fee paid by such alien shall be refunded.\n#### 5. Termination of Diversity Immigrant Visa Program\n##### (a) Repeal\nSection 203 of the Immigration and Nationality Act ( 8 U.S.C. 1153 ) is amended by striking subsection (c).\n##### (b) Technical and conforming amendments\nTitle II of the Immigration and Nationality Act ( 8 U.S.C. 1151 et seq. ) is amended\u2014\n**(1)**\nin section 201\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by adding and at the end;\n**(ii)**\nin paragraph (2), by striking ; and and inserting a period; and\n**(iii)**\nby striking paragraph (3); and\n**(B)**\nby striking subsection (e);\n**(2)**\nin section 203\u2014\n**(A)**\nby striking subsection (c);\n**(B)**\nin subsection (d), by striking subsection (a), (b), or (c) and inserting subsection (a) or (b) ;\n**(C)**\nin subsection (e)\u2014\n**(i)**\nby striking paragraph (2); and\n**(ii)**\nby redesignating paragraph (3) as paragraph (2);\n**(D)**\nin subsection (f), by striking subsection (a), (b), or (c) of this section and inserting subsection (a) or (b) ;\n**(E)**\nin subsection (g), by striking subsections (a), (b), and (c) and inserting subsections (a) and (b) ; and\n**(F)**\nin subsection (h)(2)(B), by striking subsection (a), (b), or (c) and inserting subsection (a) or (b) ; and\n**(3)**\nin section 204\u2014\n**(A)**\nin subsection (a)(1), by striking subparagraph (I);\n**(B)**\nin subsection (e), by striking subsection (a), (b), or (c) and inserting subsection (a) or (b) ; and\n**(C)**\nin subsection (l)(2)(B), by striking section 203 (a) or (d) and inserting subsection (a) or (d) of section 203 .\n##### (c) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall take effect on the date of the enactment of this Act.\n**(2) Selectees**\nNotwithstanding paragraph (1), in the case of any alien who registered for the Diversity Immigrant Visa Program and received notification before the date of the enactment of this Act that he or she has been selected to apply for a diversity immigrant visa under section 203(c) of the Immigration and Nationality Act ( 8 U.S.C. 1153(c) ), such application shall be revoked, and any fee paid by such alien shall be refunded.\n#### 6. Definition\nTerms used in this Act have the meaning given such terms under section 101(a) of the Immigration and Nationality Act.",
      "versionDate": "2025-11-20",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-12-12T16:17:32Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6225ih.xml"
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
      "title": "PAUSE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAUSE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pausing on Admissions Until Security Ensured Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for a limitation on the ability to issue any visa or provide any status under the immigration laws until certain conditions have been met.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T07:18:31Z"
    }
  ]
}
```
