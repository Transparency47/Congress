# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/68?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/68
- Title: Complete COVID Collections Act
- Congress: 119
- Bill type: S
- Bill number: 68
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2026-02-02T22:05:16Z
- Update date including text: 2026-02-02T22:05:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-05 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with amendments favorably.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with amendments. Without written report.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with amendments. Without written report.
- 2025-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 8.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-02-05 - Committee: Committee on Small Business and Entrepreneurship. Ordered to be reported with amendments favorably.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with amendments. Without written report.
- 2025-02-10 - Committee: Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with amendments. Without written report.
- 2025-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 8.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/68",
    "number": "68",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
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
    "title": "Complete COVID Collections Act",
    "type": "S",
    "updateDate": "2026-02-02T22:05:16Z",
    "updateDateIncludingText": "2026-02-02T22:05:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 8.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-02-10",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Small Business and Entrepreneurship. Reported by Senator Ernst with amendments. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Ordered to be reported with amendments favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
            "date": "2025-02-10T21:39:48Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T16:15:13Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-09T21:46:24Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "IN"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "TN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "UT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MO"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s68is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 68\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Ms. Ernst (for herself, Mr. Young , Mrs. Blackburn , Mr. Lankford , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo prohibit the suspension of collections on loans made to small businesses related to COVID\u201319, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Complete COVID Collections Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administration; Administrator**\nThe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively.\n**(2) Covered funds**\nThe term covered funds means amounts made available for COVID\u201319 relief under\u2014\n**(A)**\nthe Coronavirus Preparedness and Response Supplemental Appropriations Act, 2020 ( Public Law 116\u2013123 ; 134 Stat 146);\n**(B)**\nthe Families First Coronavirus Response Act ( Public Law 116\u2013127 ; 134 Stat. 178);\n**(C)**\nthe CARES Act ( Public Law 116\u2013136 ; 134 Stat. 281);\n**(D)**\nthe Paycheck Protection Program and Health Care Enhancement Act ( Public Law 116\u2013139 ; 134 Stat. 620);\n**(E)**\ndivision M or N of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ; 134 Stat. 1909); or\n**(F)**\nthe American Rescue Plan Act of 2021 ( Public Law 117\u20132 ; 135 Stat. 4).\n**(3) Covered loan**\nThe term covered loan means\u2014\n**(A)**\na loan guaranteed under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ); and\n**(B)**\na loan made under section 7(b)(2) of the Small Business Act ( 15 U.S.C. 636(b)(2) ) related to COVID\u201319.\n**(4) Covered program**\nThe term covered program means\u2014\n**(A)**\nloans made under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) );\n**(B)**\neconomic injury disaster loans made under section 7(b)(2) of the Small Business Act ( 15 U.S.C. 636(b)(2) ) related to COVID\u201319;\n**(C)**\nadvances provided pursuant to section 1110 of the CARES Act ( 15 U.S.C. 9009 ), section 331 of division N of the Consolidated Appropriations Act, 2021 ( 15 U.S.C. 9009b ), or section 5002(b) of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009 note);\n**(D)**\nrestaurant revitalization grants made under section 5003 of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009c ); and\n**(E)**\ngrants for shuttered venue operators made under section 324 of division N of the Consolidated Appropriations Act, 2021 ( 15 U.S.C. 9009a ).\n**(5) Improper payment**\nThe term improper payment has the meaning given the term in section 3351 of title 31, United States Code.\n#### 3. Special Inspector General for Pandemic Recovery\n##### (a) Extension\nSection 4018 of the CARES Act ( 15 U.S.C. 9053 ) is amended\u2014\n**(1)**\nin subsection (c)(1), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby inserting or the Administrator of the Small Business Administration (referred to in this section as the Administrator ) after the Secretary of the Treasury ;\n**(B)**\nby inserting or the Administrator after established by the Secretary ;\n**(C)**\nby inserting or any assistance provided under any covered program after under this Act each place that term appears; and\n**(D)**\nby inserting or the Administrator after management by the Secretary ;\n**(2)**\nin subsection (h), by striking the date 5 years after March 27, 2020 and inserting September 30, 2030 ; and\n**(3)**\nby adding at the end the following:\n(k) Coordination and provision of information (1) Coordination In carrying out the duties, responsibilities, and authorities of the Special Inspector General under this section, the Special Inspector General shall coordinate with, and receive the cooperation of, the Administrator and the Inspector General of the Small Business Administration. (2) Information The Administrator shall provide data and information related to covered programs to the Special Inspector General in the same manner as the Administrator provides that data and information to the Inspector General of the Small Business Administration. (l) Covered program In this section, the term covered program has the meaning given the term in section 2 of the Complete COVID Collections Act . .\n#### 4. Fraud enforcement harmonization\n##### (a) Emergency relief and taxpayer protections\nSection 4003 of the CARES Act ( 15 U.S.C. 9042 ) is amended by adding at the end the following:\n(i) Fraud enforcement harmonization Notwithstanding any other provision of law, any criminal charge or civil enforcement action alleging that a business, State, or municipality engaged in fraud or similarly related crime with respect to any loan, loan guarantee, or other investment made under this section shall be filed not later than 10 years after the offense was committed. .\n##### (b) Grants for shuttered venue operators\nSection 324 of division N of the Consolidated Appropriations Act, 2021 ( 15 U.S.C. 9009a ) is amended by adding at the end the following:\n(g) Fraud enforcement harmonization Notwithstanding any other provision of law, any criminal charge or civil enforcement action alleging that a business, State, or municipality engaged in fraud or similarly related crime with respect to any grant made under this section shall be filed not later than 10 years after the offense was committed. .\n##### (c) Restaurant revitalization grants\nSection 5003 of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009c ) is amended by adding at the end the following:\n(d) Fraud enforcement harmonization Notwithstanding any other provision of law, any criminal charge or civil enforcement action alleging that a business, State, or municipality engaged in fraud or similarly related crime with respect to any grant made under this section shall be filed not later than 10 years after the offense was committed. .\n#### 5. Prohibition on suspending collections on SBA loans related to COVID\u201319\n##### (a) Referral of claims\nThe Administrator shall refer to the Department of the Treasury any claim for collection related to a covered loan under $100,000.\n##### (b) Department of the Treasury determination\nThe Department of the Treasury shall render a final decision as to suspend, end, or make collection on a claim referred to the Department of the Treasury by the Administrator under subsection (a).\n##### (c) Briefings and testimony\n**(1) Monthly briefings**\nNot later than 30 days after the date of enactment of this Act, and every 30 days thereafter, the Administrator shall brief the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives on the progress of the Administrator in pursuing the collection of claims related to covered loans and transferring claims to the Department of the Treasury for collection in accordance with subchapter II of chapter 37 of title 31, United States Code.\n**(2) Testimony**\n**(A) In general**\nThe Administrator shall testify annually before the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives on\u2014\n**(i)**\nthe implementation of collections of claims related to covered loans;\n**(ii)**\nimproper payments related to covered programs; and\n**(iii)**\nthe compliance of the Administration with the reporting requirements under subchapter IV of chapter 33 of title 31, United States Code.\n**(B) Nondelegation**\nThe Administrator may not delegate the responsibility under subparagraph (A) to any other individual.\n#### 6. Department of Justice COVID\u201319 program fraud report\n##### (a) Requirement\nNot later than 90 days after the date of enactment of this Act, and every month thereafter, the Attorney General shall submit to Congress a report on activities related to covered programs, which shall include\u2014\n**(1)**\na summary of the information contained in the report, specifically the total number of prosecutions, the total dollar amount recovered by prosecutions, the total number of referrals and source of such referrals, and the total number of declined cases and reasons for declining;\n**(2)**\nwith respect to each covered program\u2014\n**(A)**\nthe number and disposition of each prosecution;\n**(B)**\nthe dollar amount recovered from prosecutions;\n**(C)**\nthe number of declined cases and the reasons for declining;\n**(D)**\nthe number of referrals\u2014\n**(i)**\nfrom the Department of Justice; and\n**(ii)**\nfrom sources other than the Department of Justice, such as other inspectors general; and\n**(E)**\nthe disposition of each referral described in subparagraph (D), specifically whether the referral resulted in prosecution or declination; and\n**(3)**\nany additional matters as the Attorney General determines appropriate.\n#### 7. Recoveries transparency\nNot later than 60 days after the date of enactment of this Act, the Pandemic Response Accountability Committee established under section 15010 of division B of the CARES Act ( Public Law 116\u2013136 ; 134 Stat. 533) shall establish and maintain on the website of the Committee real-time data relating to covered funds recovered by the Federal Government, which shall be broken out by type of covered funds and dollar amount of covered funds recovered by the Federal Government.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s68rs.xml",
      "text": "II\nCalendar No. 8\n119th CONGRESS\n1st Session\nS. 68\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Ms. Ernst (for herself, Mr. Young , Mrs. Blackburn , Mr. Lankford , Mr. Curtis , Mr. Schmitt , and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nFebruary 10, 2025 Reported by Ms. Ernst , with amendments Omit the parts struck through and insert the parts printed in italic\nA BILL\nTo prohibit the suspension of collections on loans made to small businesses related to COVID\u201319, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Complete COVID Collections Act .\n#### 2. Definitions\nIn this Act:\n**(1) Administration; Administrator**\nThe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively.\n**(2) Covered funds**\nThe term covered funds means amounts made available for COVID\u201319 relief under\u2014\n**(A)**\nthe Coronavirus Preparedness and Response Supplemental Appropriations Act, 2020 ( Public Law 116\u2013123 ; 134 Stat . 146);\n**(B)**\nthe Families First Coronavirus Response Act ( Public Law 116\u2013127 ; 134 Stat. 178);\n**(C)**\nthe CARES Act ( Public Law 116\u2013136 ; 134 Stat. 281);\n**(D)**\nthe Paycheck Protection Program and Health Care Enhancement Act ( Public Law 116\u2013139 ; 134 Stat. 620);\n**(E)**\ndivision M or N of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ; 134 Stat. 1909 1182 ); or\n**(F)**\nthe American Rescue Plan Act of 2021 ( Public Law 117\u20132 ; 135 Stat. 4).\n**(3) Covered loan**\nThe term covered loan means\u2014\n**(A)**\na loan guaranteed under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ); and\n**(B)**\na loan made under section 7(b)(2) of the Small Business Act ( 15 U.S.C. 636(b)(2) ) related to COVID\u201319.\n**(4) Covered program**\nThe term covered program means\u2014\n**(A)**\nloans made under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) );\n**(B)**\neconomic injury disaster loans made under section 7(b)(2) of the Small Business Act ( 15 U.S.C. 636(b)(2) ) related to COVID\u201319;\n**(C)**\nadvances provided pursuant to section 1110 of the CARES Act ( 15 U.S.C. 9009 ), section 331 of division N of the Consolidated Appropriations Act, 2021 ( 15 U.S.C. 9009b ), or section 5002(b) of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009 note);\n**(D)**\nrestaurant revitalization grants made under section 5003 of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009c ); and\n**(E)**\ngrants for shuttered venue operators made under section 324 of division N of the Consolidated Appropriations Act, 2021 ( 15 U.S.C. 9009a ).\n**(5) Improper payment**\nThe term improper payment has the meaning given the term in section 3351 of title 31, United States Code.\n#### 3. Special Inspector General for Pandemic Recovery\n##### (a) Extension\nSection 4018 of the CARES Act ( 15 U.S.C. 9053 ) is amended\u2014\n**(1)**\nin subsection (c)(1), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby inserting or the Administrator of the Small Business Administration (referred to in this section subsection as the Administrator ) after the Secretary of the Treasury ;\n**(B)**\nby inserting or the Administrator after established by the Secretary ;\n**(C)**\nby inserting or any assistance provided under any covered program after under this Act each place that term appears; and\n**(D)**\nby inserting or the Administrator after management by the Secretary ;\n**(2)**\nin subsection (h), by striking the date 5 years after March 27, 2020 the enactment of this Act and inserting September 30, 2030 ; and\n**(3)**\nby adding at the end the following:\n(k) Coordination and provision of information (1) Coordination In carrying out the duties, responsibilities, and authorities of the Special Inspector General under this section, the Special Inspector General shall coordinate with, and receive the cooperation of, the Administrator of the Small Business Administration and the Inspector General of the Small Business Administration. (2) Information The Administrator of the Small Business Administration shall provide data and information related to covered programs to the Special Inspector General in the same manner as the Administrator provides that data and information to the Inspector General of the Small Business Administration. (l) Covered program In this section, the term covered program has the meaning given the term in section 2 of the Complete COVID Collections Act . .\n#### 4. Fraud enforcement harmonization\n##### (a) Emergency relief and taxpayer protections\nSection 4003 of the CARES Act ( 15 U.S.C. 9042 ) is amended by adding at the end the following:\n(i) Fraud enforcement harmonization Notwithstanding any other provision of law, any criminal charge or civil enforcement action alleging that a business, State, or municipality engaged in fraud or similarly related crime with respect to any loan, loan guarantee, or other investment made under this section shall be filed not later than 10 years after the offense was committed. .\n##### (b) Grants for shuttered venue operators\nSection 324 of division N of the Consolidated Appropriations Act, 2021 ( 15 U.S.C. 9009a ) is amended by adding at the end the following:\n(g) Fraud enforcement harmonization Notwithstanding any other provision of law, any criminal charge or civil enforcement action alleging that a business, State, or municipality an eligible person or entity engaged in fraud or similarly related crime with respect to any grant made under this section shall be filed not later than 10 years after the offense was committed. .\n##### (c) Restaurant revitalization grants\nSection 5003 of the American Rescue Plan Act of 2021 ( 15 U.S.C. 9009c ) is amended by adding at the end the following:\n(d) Fraud enforcement harmonization Notwithstanding any other provision of law, any criminal charge or civil enforcement action alleging that a business, State, or municipality an eligible entity engaged in fraud or similarly related crime with respect to any grant made under this section shall be filed not later than 10 years after the offense was committed. .\n#### 5. Prohibition on suspending collections on SBA loans related to COVID\u201319\n##### (a) Referral of claims\nThe Administrator shall refer to the Department of the Treasury any claim for collection related to a covered loan under $100,000.\n##### (b) Department of the Treasury determination\nThe Department of the Treasury shall render a final decision as to suspend, end, or make collection on a claim referred to the Department of the Treasury by the Administrator under subsection (a).\n##### (c) Briefings and testimony\n**(1) Monthly briefings**\nNot later than 30 days after the date of enactment of this Act, and every 30 days thereafter, the Administrator shall brief the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives on the progress of the Administrator in pursuing the collection of claims related to covered loans and transferring claims to the Department of the Treasury for collection in accordance with subchapter II of chapter 37 of title 31, United States Code.\n**(2) Testimony**\n**(A) In general**\nThe Administrator shall testify annually before the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business of the House of Representatives on\u2014\n**(i)**\nthe implementation of collections of claims related to covered loans;\n**(ii)**\nimproper payments related to covered programs; and\n**(iii)**\nthe compliance of the Administration with the reporting requirements under subchapter IV of chapter 33 of title 31, United States Code.\n**(B) Nondelegation**\nThe Administrator may not delegate the responsibility under subparagraph (A) to any other individual.\n#### 6. Department of Justice COVID\u201319 program fraud report\n##### (a) Requirement\nNot later than 90 days after the date of enactment of this Act, and every month thereafter, the Attorney General shall submit to Congress a report on activities of the Department of Justice related to covered programs, which shall include\u2014\n**(1)**\na summary of the information contained in the report, specifically the total number of prosecutions, the total dollar amount recovered by prosecutions, the total number of referrals and source of such referrals, and the total number of declined cases and reasons for declining;\n**(2)**\nwith respect to each covered program\u2014\n**(A)**\nthe number of prosecutions and disposition of each prosecution;\n**(B)**\nthe dollar amount recovered from prosecutions;\n**(C)**\nthe number of declined cases and the reasons for declining;\n**(D)**\nthe number of referrals\u2014\n**(i)**\nfrom the Department of Justice; and\n**(ii)**\nfrom sources other than the Department of Justice, such as other inspectors general of other agencies ; and\n**(E)**\nthe disposition of each referral described in subparagraph (D), specifically whether the referral resulted in prosecution or declination; and\n**(3)**\nany additional matters as the Attorney General determines appropriate.\n#### 7. Recoveries transparency\nNot later than 60 days after the date of enactment of this Act, the Pandemic Response Accountability Committee established under section 15010 of division B of the CARES Act ( Public Law 116\u2013136 ; 134 Stat. 533) shall establish and maintain on the website of the Committee real-time data relating to covered funds recovered by the Federal Government, which shall be broken out by type of covered funds and dollar amount of covered funds recovered by the Federal Government.\n#### 8. Fraud recovery collections\nAny collection of amounts that were obtained through a covered program as a result of fraud shall be applied solely towards reduction of the Federal debt.",
      "versionDate": "2025-02-10",
      "versionType": "Reported in Senate"
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
            "name": "Debt collection",
            "updateDate": "2025-03-13T14:51:34Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-03-13T14:50:19Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-03-13T14:51:54Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-13T14:52:21Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-03-13T14:50:56Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-13T14:50:32Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-13T14:50:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-03T12:25:36Z"
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
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s68is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s68rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Complete COVID Collections Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "title": "Complete COVID Collections Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Complete COVID Collections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T14:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the suspension of collections on loans made to small businesses related to COVID-19, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T14:18:25Z"
    }
  ]
}
```
