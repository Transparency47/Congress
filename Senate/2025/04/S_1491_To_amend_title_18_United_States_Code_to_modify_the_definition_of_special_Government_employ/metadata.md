# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1491?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1491
- Title: SEER Act 2025
- Congress: 119
- Bill type: S
- Bill number: 1491
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-01-14T05:05:17Z
- Update date including text: 2026-01-14T05:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1491",
    "number": "1491",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "SEER Act 2025",
    "type": "S",
    "updateDate": "2026-01-14T05:05:17Z",
    "updateDateIncludingText": "2026-01-14T05:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-11T02:35:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MI"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MD"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "HI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "VT"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "AZ"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1491is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1491\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Ms. Warren (for herself, Mr. Schumer , Mr. Peters , Mr. Luj\u00e1n , Mr. Merkley , Mr. Blumenthal , Mr. Van Hollen , Ms. Hirono , Mr. Padilla , Mr. Schiff , Mr. Welch , and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 18, United States Code, to modify the definition of special Government employee, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SGE Ethics Enforcement Reform Act of 2025 or the SEER Act 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSome special Government employees have substantial financial conflicts of interest due to their other business activities while in Federal service.\n**(2)**\nSpecial Government employees are subject to the criminal conflict-of-interest statute applicable to full-time Government employees, section 208 of title 18, United States Code. However, Federal employees, including special Government employees, do not have to resolve conflicts under that provision if the relevant work does not constitute a particular matter.\n**(3)**\nUnlike senior executive branch employees under chapter 131 of title 5, United States Code, the vast majority of special Government employees are not required to make their financial disclosure reports public, thus concealing from the public their potential financial conflicts of interest.\n**(4)**\nThe vast majority of special Government employees in the Federal Government serve on advisory committees and have a limited role in Government decision-making. But a select number of special Government employees have assumed authority within the Federal Government commensurate with a senior or very senior full-time Federal employee.\n**(5)**\nThe executive branch has not notified the public or Congress when it uses special Government employees to perform high-level responsibilities.\n**(6)**\nThe executive branch has permitted employees to retain special Government employee status beyond the statutory limit of 130 days during any period of 365 consecutive days.\n#### 3. Conflicts of interest\nTitle 18, United States Code, is amended\u2014\n**(1)**\nin section 202(a), in the first sentence, by inserting and who has been designated as a special Government employee on a Notification of Personnel Action (Standard Form 50 or equivalent) of the officer or employee, after basis, ; and\n**(2)**\nin section 208\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nby striking (a) Except and inserting (a)(1) Except ; and\n**(ii)**\nby adding at the end the following:\n(2) In the case of a special Government employee who is not on an advisory committee or who serves as the chair or vice chair of an advisory committee, paragraph (1) shall apply to a discrete and identifiable component of a matter that on its own would constitute a particular matter in which, to the knowledge of the special Government employee, the organization in which the special Government employee is serving as officer, director, trustee, general partner, or employee has a financial interest. ;\n**(B)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), by inserting , with the concurrence of a designated official at the Office of Government Ethics if the officer or employee is a special Government employee, after such official ; and\n**(ii)**\nin paragraph (3), by inserting , other than the chair or vice chair of the committee, after committee ;\n**(C)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (1), in the first sentence, by striking Upon and inserting Except as provided in paragraph (2), upon ;\n**(ii)**\nby redesignating paragraph (2) as paragraph (3); and\n**(iii)**\nby inserting after paragraph (1) the following:\n(2) In the case of a special Government employee who is not serving on an advisory committee within the meaning of chapter 10 of title 5 or a special Government employee who is serving as chair or vice chair on such an advisory committee, any waiver or exemption granted under subsection (b)(1) shall be proactively made publicly available via a searchable online database not later than 14 days after the date on which the waiver is issued. .\n#### 4. Restriction on communications with agencies\n##### (a) Definition\nIn this section, the term large company means\u2014\n**(1)**\nany for-profit company that has greater than an average of $1,000,000,000 in market capitalization or revenue for the previous 3-year period;\n**(2)**\nany Federal contractor that received greater than $100,000,000 in annual revenue from the Federal Government during the previous 3-year period; and\n**(3)**\nany for-profit company that exerts monopolistic or monopsonistic control over a significant share of the market in its particular industry, as defined by regulation by the Director of the Office of Government Ethics, in consultation with the Attorney General.\n##### (b) Restriction\nNo special Government employee, as defined in section 202 of title 18, United States Code, who is not on an advisory committee or a chair or vice chair on an advisory committee may have direct or indirect communications in their official capacity with an agency or office that contracts with, regulates, or has a pending enforcement action against a large company\u2014\n**(1)**\nthat the special Government employee owns; or\n**(2)**\nfor which the special Government employee serves as a senior executive or director.\n##### (c) Regulations\nThe Office of Government Ethics shall promulgate regulations carrying out this section, including to define ownership of a large company.\n#### 5. Database of special Government employees\nSection 1103 of title 5, United States Code, is amended by adding at the end the following:\n(d) (1) In this subsection, the term covered individual \u2014 (A) means an individual who is a special Government employee who is not serving on an advisory committee; and (B) does not include an individual described in paragraph (1) or (2) of section 13107(a). (2) The Director, in coordination with the Office of Government Ethics, shall maintain to the extent technically practicable, keep current, and make available to the public over the internet, without a fee or other access charge, in a searchable, sortable, and downloadable manner, an electronic database that contains the name of each covered individual, a rolling tally of the number of days the person has served as a special Government employee, and a description of why the individual was designated as a special Government employee rather than a regular employee. .\n#### 6. Financial disclosure requirements of special Government employees\nTitle 5, United States Code, is amended\u2014\n**(1)**\nin section 13103(f)\u2014\n**(A)**\nin paragraph (8), by striking (other than a special Government employee) ;\n**(B)**\nin paragraph (11), by striking and at the end ;\n**(C)**\nin paragraph (12), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(13) A special Government employee who\u2014 (A) is not serving on an advisory committee or is serving as a chair or vice chair on an advisory committee; and (B) is not serving in a position classified as a general schedule position at the GS\u20139 level or below, with limited responsibilities, closely supervised by a career Federal employee. (14) For any special Government employee claiming an exemption from filing a public report this subsection, the relevant agency ethics officer shall review to ensure the exemption may be properly applied to that special Government employee. ; and\n**(2)**\nin section 13109(a)(1), by inserting , except as provided in section 13103(f)(13), after title 18) .\n#### 7. Modifications of online access to certain financial disclosure statements and related forms\nSection 1(a)(2) of the Act entitled An Act to modify the requirements under the STOCK Act regarding online access to certain financial disclosure statements and related forms , approved April 15, 2013 ( 5 U.S.C. 13107 note) is amended by adding at the end the following:\n(F) Any special Government employee of the executive branch who\u2014 (i) is not serving on an advisory committee or is serving as a chair or vice chair on an advisory committee; or (ii) is not serving in a position classified as a general schedule position at the GS\u20139 level or below, with limited responsibilities, closely supervised by a career Federal employee. .\n#### 8. Special Government employee rule\n##### (a) In general\nExcept as provided in subsection (b), in the case of a special Government employee, as defined in section 202 of title 18, United States Code, who has served in their department or agency for more than 60 days during the immediately preceding period of 365 consecutive days, all Federal ethics rules shall apply to such special Government employee to the same extent that such rules apply to regular Government employees.\n##### (b) Exception\nIn the case of a special Government employee, as defined in section 202 of title 18, United States Code, who has served in their department or agency for more than 130 during the immediately preceding period of 365 consecutive days, section 209 of title 18, United States Code, and subchapter III of chapter 131 of title 5, United States Code, shall apply to such special Government employee to the same extent that the section applies to regular Government employees, except that such section 209 shall apply whether the special Government employee serves with or without pay.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2894",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SEER Act of 2025",
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
        "updateDate": "2025-05-27T15:50:34Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1491is.xml"
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
      "title": "SEER Act 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SEER Act 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SGE Ethics Enforcement Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to modify the definition of special Government employee, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:25Z"
    }
  ]
}
```
