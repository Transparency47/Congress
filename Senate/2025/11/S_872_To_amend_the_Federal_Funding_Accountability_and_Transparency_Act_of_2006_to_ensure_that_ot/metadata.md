# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/872?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/872
- Title: Stop Secret Spending Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 872
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-03-19T11:03:26Z
- Update date including text: 2026-03-19T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2025-11-07 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with amendments. Without written report.
- 2025-11-07 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with amendments. Without written report.
- 2025-11-07 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 265.
- 2026-03-18 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.
- 2025-11-07 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with amendments. Without written report.
- 2025-11-07 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with amendments. Without written report.
- 2025-11-07 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 265.
- 2026-03-18 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/872",
    "number": "872",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Stop Secret Spending Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:26Z",
    "updateDateIncludingText": "2026-03-19T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 265.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2026-03-18T18:30:02Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": [
          {
            "date": "2025-11-07T18:41:53Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:18Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-05T21:18:32Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "OK"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "FL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s872is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 872\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Ms. Ernst (for herself, Mr. Peters , Mr. Lankford , and Mr. Moreno ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend the Federal Funding Accountability and Transparency Act of 2006 to ensure that other transaction agreements are reported to USAspending.gov, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Secret Spending Act of 2025 .\n#### 2. Other transaction agreement reporting\n##### (a) Other transaction agreements\nSection 2(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(1)**\nin paragraph (4)(A)\u2014\n**(A)**\nin clause (ii), by adding and and the end; and\n**(B)**\nby adding at the end the following:\n(iii) includes other transaction agreements; ; and\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nin subparagraph (B), by striking (2)(A)(i) and inserting (4)(A)(i) ; and\n**(B)**\nin subparagraph (C), by striking (2)(A)(ii) and inserting (4)(A)(ii) .\n##### (b) Data standards\nSection 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended by adding at the end the following:\n(e) Other transaction agreement data Not later than 3 years after the date of enactment of the Stop Secret Spending Act of 2025 , the Secretary shall ensure that, with respect to the website established under section 2, or any successor website\u2014 (1) data relating to other transaction agreements is automatically transmitted to the website, and (2) a centralized view of the data described in paragraph (1) is available on the website. .\n##### (c) Annual report on unreported funding\nSection 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended by adding at the end the following:\n(h) Annual report Not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 , and annually thereafter, the Secretary, in consultation with the Director, shall post to the website established under this section a report that includes\u2014 (1) the total amount of Federal spending on Federal awards for which data has not been posted to the website; and (2) the reason data on the Federal spending described in paragraph (1) has not been posted to the website, including whether the Federal spending was\u2014 (A) national security-related or classified; (B) a grant or contract awarded or entered into by a legislative or judicial branch agency; or (C) a subaward below a primary subaward. .\n##### (d) Implementation plan\n**(1) Definitions**\nIn this subsection:\n**(A) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(B) Relevant agency**\nThe term relevant agency means a Federal agency (as defined in section 2(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note)) that has the authority to enter into an other transaction agreement, as determined by the Director.\n**(C) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(D) USAspending.gov**\nThe term USAspending.gov means the website established under section 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).\n**(2) Initial compilation**\nIf the Secretary has not yet complied with subsection (e) of section 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by this section, by the date that is 1 year after the date of enactment of this Act, not later than 1 year after the date of enactment of this Act, the Secretary, in coordination with the Director and the heads of relevant agencies, shall publish on USAspending.gov a report that lists and includes a detailed description of all other transaction agreements entered into by the relevant agencies for the fiscal year preceding the fiscal year during which the report is published.\n**(3) Plan**\nIf the Secretary has not yet complied with subsection (e) of section 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by this section, by the date that is 2 years after the date of enactment of this Act, not later than 2 years after the date of enactment of this Act, the Secretary, in consultation with the Director and the heads of relevant agencies, shall submit to Congress a plan that includes\u2014\n**(A)**\nthe status of including data relating to other transaction agreements on USAspending.gov; and\n**(B)**\nactions underway and planned to ensure that the data described in subparagraph (A) is fully incorporated into USAspending.gov by the date that is 3 years after the date of enactment of this Act.\n#### 3. Other amendments\n##### (a) Inspector General reports\nSection 6(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking each Federal agency and inserting each agency described in paragraphs (1) and (2) of section 901(b) of title 31, United States Code ;\n**(B)**\nin subparagraph (A), by striking Federal agency and inserting agency ; and\n**(C)**\nin subparagraph (B), by striking Federal agency and inserting agency ; and\n**(2)**\nby striking paragraph (2) and inserting the following:\n(2) Deadlines The inspector general of each agency described in paragraphs (1) and (2) of section 901(b) of title 31, United States Code, shall submit to Congress and make publicly available a report described in paragraph (1)(B)\u2014 (A) not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 ; and (B) not less than frequently than once every 2 years after the date described in subparagraph (A) until the date that is 10 years after the date of enactment of the Stop Secret Spending Act of 2025 on the date of submission of the report required under section 3521(f) or 9105(a)(3) of title 31, United States Code, for the applicable fiscal year. .\n##### (b) Full disclosure of Federal funds\n**(1) In general**\nSection 3 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nparagraph (1), in the matter preceding subparagraph (A), by striking a Federal agency or component of a Federal agency and inserting a Federal agency or a component of a Federal agency included on the list posted under subsection (e)(2) ; and\n**(ii)**\nin paragraph (2)(B), in the matter preceding clause (i), by striking to be posted and inserting to be posted by a Federal agency or a component of a Federal agency included on the list posted under subsection (e)(2) ; and\n**(B)**\nby adding at the end the following:\n(c) Quality of information (1) In general The Secretary and the Director, in consultation with the heads of Federal agencies, shall establish requirements to ensure that the information to be posted under subsection (b) that is posted by a Federal agency or component of a Federal agency is complete and accurate. (2) Federal agency responsibility The head of each Federal agency or component of a Federal agency posting data under subsection (b) shall ensure that the data is complete and accurate. (3) Authority to verify accuracy The Secretary and the Director may verify that the data posted under subsection (b) by a Federal agency or component of a Federal agency are complete, accurate, and consistent. (d) Display standards The Secretary, in consultation with the Director, shall ensure that the heads of Federal agencies that post information under subsection (b) comply with display standards established by the Secretary. (e) Agency reporting determination Not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 , and not less frequently than once every 2 years thereafter, the Secretary, in coordination with the Director, shall\u2014 (1) assess and make a determination with respect to which Federal agencies and components of Federal agencies are required to post information under subsection (b); (2) publish a list of the Federal agencies and components of Federal agencies determined under paragraph (1) on the website established under section 2(b)(1); and (3) provide to the head and inspector general of each Federal agency or component of a Federal agency included on the list published under paragraph (2) written notice of the inclusion of the Federal agency or component of a Federal agency on the list. .\n**(2) Effective date**\nThe amendments made by paragraph (1)(A) shall take effect on the date on which the Secretary publishes the first list under section 3(e)(2) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by paragraph (1).\n#### 4. GAO report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall make recommendations for any updates the Comptroller General of the United States determines advisable to clause 52.204.10 of the Federal Acquisition Regulation with respect to incorporating requirements under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s872rs.xml",
      "text": "II\nCalendar No. 265\n119th CONGRESS\n1st Session\nS. 872\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Ms. Ernst (for herself, Mr. Peters , Mr. Lankford , Mr. Moreno , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nNovember 7, 2025 Reported by Mr. Paul , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo amend the Federal Funding Accountability and Transparency Act of 2006 to ensure that other transaction agreements are reported to USAspending.gov, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Secret Spending Act of 2025 .\n#### 2. Other transaction agreement reporting\n##### (a) Other transaction agreements\nSection 2(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(1)**\nin paragraph (4)(A)\u2014\n**(A)**\nin clause (ii), by adding or and and the end; and\n**(B)**\nby adding at the end the following:\n(iii) includes include other transaction agreements; ; and\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nin subparagraph (B), by striking (2)(A)(i) and inserting (4)(A)(i) ; and\n**(B)**\nin subparagraph (C), by striking (2)(A)(ii) and inserting (4)(A)(ii) .\n##### (b) Data standards\nSection 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended by adding at the end the following:\n(e) Other transaction agreement data Not later than 3 years after the date of enactment of the Stop Secret Spending Act of 2025 , the Secretary shall ensure that, with respect to the website established under section 2, or any successor website\u2014 (1) data relating to other transaction agreements is automatically transmitted to the website , ; and (2) a centralized view of the data described in paragraph (1) is available on the website. .\n##### (c) Annual report on unreported funding\nSection 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended by adding at the end the following:\n(h) Annual report Not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 , and annually thereafter, the Secretary, in consultation with the Director, shall post to the website established under this section a report that includes\u2014 (1) the total amount of Federal spending on Federal awards for which data has not been posted to the website; and (2) the reason data on the Federal spending described in paragraph (1) has not been posted to the website, including whether the Federal spending was\u2014 (A) national security-related or classified; (B) a grant or contract awarded or entered into by a legislative or judicial branch agency; or (C) a subaward below a primary subaward. .\n##### (d) Implementation plan\n**(1) Definitions**\nIn this subsection:\n**(A) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(B) Relevant agency**\nThe term relevant agency means a Federal agency (as defined in section 2(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note)) that has the authority to enter into an other transaction agreement, as determined by the Director.\n**(C) Secretary**\nThe term Secretary means the Secretary of the Treasury.\n**(D) USAspending.gov**\nThe term USAspending.gov means the website established under section 2 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).\n**(2) Initial compilation**\nIf the Secretary has not yet complied with subsection (e) of section 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by this section, by the date that is 1 year after the date of enactment of this Act, not later than 1 year after the date of enactment of this Act, the Secretary, in coordination with the Director and the heads of relevant agencies, shall publish on USAspending.gov a report that lists and includes a detailed description of all other transaction agreements entered into by the relevant agencies for the fiscal year preceding the fiscal year during which the report is published.\n**(3) Plan**\nIf the Secretary has not yet complied with subsection (e) of section 4 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by this section, by the date that is 2 years after the date of enactment of this Act, not later than 2 years after the date of enactment of this Act, the Secretary, in consultation with the Director and the heads of relevant agencies, shall submit to Congress a plan that includes\u2014\n**(A)**\nthe status of including data relating to other transaction agreements on USAspending.gov; and\n**(B)**\nactions underway and planned to ensure that the data described in subparagraph (A) is fully incorporated into USAspending.gov by the date that is 3 years after the date of enactment of this Act.\n#### 3. Other amendments\n##### (a) Inspector General reports\nSection 6(a) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking each Federal agency and inserting each agency described in paragraphs (1) and (2) paragraph (1) or (2) of section 901(b) of title 31, United States Code ;\n**(B)**\nin subparagraph (A), by striking Federal agency and inserting agency ; and\n**(C)**\nin subparagraph (B), by striking Federal agency and inserting agency ; and\n**(2)**\nby striking paragraph (2) and inserting the following:\n(2) Deadlines The inspector general of each agency described in paragraphs (1) and (2) paragraph (1) or (2) of section 901(b) of title 31, United States Code, shall submit to Congress and make publicly available a report described in paragraph (1)(B)\u2014 (A) not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 ; and (B) not less than frequently than once every 2 years after the date described in subparagraph (A) until the date that is 10 years after the date of enactment of the Stop Secret Spending Act of 2025 on the date of submission of the report required under section 3521(f) or 9105(a)(3) of title 31, United States Code, for the applicable fiscal year. .\n##### (b) Full disclosure of Federal funds\n**(1) In general**\nSection 3 of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note) is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nparagraph (1), in the matter preceding subparagraph (A), by striking a Federal agency or component of a Federal agency and inserting a Federal agency or a component of a Federal agency included on the list posted under subsection (e)(2) ; and\n**(ii)**\nin paragraph (2)(B), in the matter preceding clause (i), by striking to be posted and inserting to be posted by a Federal agency or a component of a Federal agency included on the list posted under subsection (e)(2) ; and\n**(B)**\nby adding at the end the following:\n(c) Quality of information (1) In general The Secretary and the Director, in consultation with the heads of Federal agencies, shall establish requirements to ensure that the information to be posted under subsection (b) that is posted by a Federal agency or component of a Federal agency is complete and accurate. (2) Federal agency responsibility The head of each Federal agency or component of a Federal agency posting data under subsection (b) shall ensure that the data is complete and accurate. (3) Authority to verify accuracy The Secretary and the Director may verify that the data posted under subsection (b) by a Federal agency or component of a Federal agency are complete, accurate, and consistent. (d) Display standards The Secretary, in consultation with the Director, shall ensure that the heads of Federal agencies that post information under subsection (b) comply with display standards established by the Secretary. (e) Agency reporting determination Not later than 1 year after the date of enactment of the Stop Secret Spending Act of 2025 , and not less frequently than once every 2 years thereafter, the Secretary, in coordination with the Director, shall\u2014 (1) assess and make a determination with respect to which Federal agencies and components of Federal agencies are required to post information under subsection (b); (2) publish a list of the Federal agencies and components of Federal agencies determined under paragraph (1) on the website established under section 2(b)(1); and (3) provide to the head and inspector general of each Federal agency or component of a Federal agency included on the list published under paragraph (2) written notice of the inclusion of the Federal agency or component of a Federal agency on the list. .\n**(2) Effective date**\nThe amendments made by paragraph (1)(A) shall take effect on the date on which the Secretary publishes the first list under section 3(e)(2) of the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note), as added by paragraph (1).\n#### 4. GAO report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall make recommendations for any updates the Comptroller General of the United States determines advisable to clause 52.204.10 52.204\u201410 of the Federal Acquisition Regulation with respect to incorporating requirements under the Federal Funding Accountability and Transparency Act of 2006 ( 31 U.S.C. 6101 note).",
      "versionDate": "2025-11-07",
      "versionType": "Reported in Senate"
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
        "actionDate": "2026-03-18",
        "text": "Committee Consideration and Mark-up Session Held"
      },
      "number": "2069",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Secret Spending Act of 2025",
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
            "name": "Budget deficits and national debt",
            "updateDate": "2025-08-07T17:51:42Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-07T17:51:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-07T17:51:42Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-08-07T17:51:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T13:49:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119s872",
          "measure-number": "872",
          "measure-type": "s",
          "orig-publish-date": "2025-03-05",
          "originChamber": "SENATE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s872v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Secret Spending Act of 2025</strong></p><p>This bill expands a requirement for federal agencies to report expenditures on the USAspending.gov website to include <em>other transaction agreement </em>expenditures. (Other transaction agreements, or OTAs, are contractual instruments other than standard procurement contracts, grants, or cooperative agreements; they are exempt from many federal procurement laws and regulations).</p><p>Under current law, federal agencies must report expenditures on federal awards to USAspending.gov with the term <em>federal award</em> defined as federal grants, loans, cooperative agreements, contracts, and certain other types of expenditures. This bill expands the definition of federal award to include expenditures under OTAs, and therefore such expenditures must be included on the USAspending.gov website.\u00a0</p><p>The Department of the Treasury must ensure that data relating to OTAs are automatically transmitted to the website and a centralized view of this data is available on the website.\u00a0Treasury must also annually post on the\u00a0USAspending.gov website a report that includes (1) the total amount of federal spending on federal awards for which data has not been posted on the website, and (2) the reason why such spending data was not posted.</p><p>For 10 years after enactment, the Office of Inspector General of specified federal agencies must periodically submit to Congress and make publicly available a report assessing the agency's spending data and use of data standards.</p>"
        },
        "title": "Stop Secret Spending Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s872.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Secret Spending Act of 2025</strong></p><p>This bill expands a requirement for federal agencies to report expenditures on the USAspending.gov website to include <em>other transaction agreement </em>expenditures. (Other transaction agreements, or OTAs, are contractual instruments other than standard procurement contracts, grants, or cooperative agreements; they are exempt from many federal procurement laws and regulations).</p><p>Under current law, federal agencies must report expenditures on federal awards to USAspending.gov with the term <em>federal award</em> defined as federal grants, loans, cooperative agreements, contracts, and certain other types of expenditures. This bill expands the definition of federal award to include expenditures under OTAs, and therefore such expenditures must be included on the USAspending.gov website.\u00a0</p><p>The Department of the Treasury must ensure that data relating to OTAs are automatically transmitted to the website and a centralized view of this data is available on the website.\u00a0Treasury must also annually post on the\u00a0USAspending.gov website a report that includes (1) the total amount of federal spending on federal awards for which data has not been posted on the website, and (2) the reason why such spending data was not posted.</p><p>For 10 years after enactment, the Office of Inspector General of specified federal agencies must periodically submit to Congress and make publicly available a report assessing the agency's spending data and use of data standards.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s872"
    },
    "title": "Stop Secret Spending Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Secret Spending Act of 2025</strong></p><p>This bill expands a requirement for federal agencies to report expenditures on the USAspending.gov website to include <em>other transaction agreement </em>expenditures. (Other transaction agreements, or OTAs, are contractual instruments other than standard procurement contracts, grants, or cooperative agreements; they are exempt from many federal procurement laws and regulations).</p><p>Under current law, federal agencies must report expenditures on federal awards to USAspending.gov with the term <em>federal award</em> defined as federal grants, loans, cooperative agreements, contracts, and certain other types of expenditures. This bill expands the definition of federal award to include expenditures under OTAs, and therefore such expenditures must be included on the USAspending.gov website.\u00a0</p><p>The Department of the Treasury must ensure that data relating to OTAs are automatically transmitted to the website and a centralized view of this data is available on the website.\u00a0Treasury must also annually post on the\u00a0USAspending.gov website a report that includes (1) the total amount of federal spending on federal awards for which data has not been posted on the website, and (2) the reason why such spending data was not posted.</p><p>For 10 years after enactment, the Office of Inspector General of specified federal agencies must periodically submit to Congress and make publicly available a report assessing the agency's spending data and use of data standards.</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s872"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s872is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s872rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Stop Secret Spending Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Stop Secret Spending Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-11T06:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Secret Spending Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Funding Accountability and Transparency Act of 2006 to ensure that other transaction agreements are reported to USAspending.gov, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:33:23Z"
    }
  ]
}
```
