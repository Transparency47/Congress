# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6517?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6517
- Title: To modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6517
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2026-05-22T08:08:10Z
- Update date including text: 2026-05-22T08:08:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-09 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6517",
    "number": "6517",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "To modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:10Z",
    "updateDateIncludingText": "2026-05-22T08:08:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-09T17:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DC"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6517ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6517\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Case (for himself, Ms. Norton , and Mr. Tonko ) introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes.\n#### 1. Librarian of Congress\n##### (a) Appointment\nThe Librarian of Congress shall be appointed by the adoption by Congress of a concurrent resolution. The concurrent resolution shall provide for the appointment of the individual selected by the commission established under subsection (b).\n##### (b) Commission\nThere is established a commission for the purposes of recommending an individual to be appointed as Librarian of Congress under subsection (a). The commission established under this subsection shall consist of the following:\n**(1)**\nThe Speaker and minority leader of the House of Representatives.\n**(2)**\nThe majority and minority leaders of the Senate.\n**(3)**\nOne Republican and Democrat Member each from the Joint Committee of Congress on the Library.\n##### (c) Term of service\nThe Librarian of Congress shall be appointed for a term of 10 years.\n##### (d) Removal\nThe Librarian of Congress may be removed from office at any time upon an affirmative vote of three-fifths of the Members duly chosen or sworn in the Senate and the House of Representatives.\n##### (e) Conforming amendment\nThe Librarian of Congress Succession Modernization Act of 2015 ( 2 U.S.C. 136 et seq. ) is repealed.\n#### 2. Comptroller General\n##### (a) In general\nSection 703 of title 31, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (a) through (f) as subsections (b) through (g), respectively;\n**(2)**\nby inserting before subsection (b), as redesignated by paragraph (1), the following:\n(a) The Comptroller General shall be appointed by the adoption by Congress of a concurrent resolution. The concurrent resolution shall provide for the appointment of the individual selected by the commission established under subsection (b)(2). ;\n**(3)**\nin subsection (b), as so redesignated\u2014\n**(A)**\nin paragraph (1), by striking Comptroller General and Deputy Comptroller General are and inserting Deputy Comptroller General is ;\n**(B)**\nin paragraph (2), in the matter before subparagraph (A), by striking the President and inserting the Congress or the President, respectively, ; and\n**(C)**\nby amending paragraph (3) to read as follows:\n(3) A commission established because of a vacancy in the office of the Comptroller General shall recommend one individual. The Congress may ask the commission to recommend additional individuals. ; and\n**(4)**\nin subsection (f)(1)(B), as so redesignated, by striking joint resolution of Congress and inserting with respect to the Comptroller General, by concurrent resolution of Congress, and with respect to the Deputy Comptroller General, by joint resolution of Congress .\n##### (b) Technical and conforming amendment\nSection 772(a) of title 31, United States Code, is amended by striking section 703(e)(1) and inserting section 703(f)(1) .\n#### 3. Director of the Government Publishing Office\nSection 301 of title 44, United States Code, is amended to read as follows:\n301. Director of the Government Publishing Office: appointment (a) The Director of the Government Publishing Office shall be appointed by the adoption by Congress of a concurrent resolution. The concurrent resolution shall provide for the appointment of the individual selected by the commission established under subsection (b). (b) There is established a commission for the purposes of recommending an individual to be appointed as Director under subsection (a). The commission established under this subsection shall consist of the following: (1) The Speaker and minority leader of the House of Representatives. (2) The majority and minority leaders of the Senate. (3) One Republican and Democrat Member each from the Joint Committee of Congress on Printing. (c) The Director may be removed from office at any time upon an affirmative vote of three-fifths of the Members duly chosen or sworn in the Senate and the House of Representatives. .",
      "versionDate": "2025-12-09",
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
        "name": "Congress",
        "updateDate": "2026-01-07T17:28:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-09",
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
          "measure-id": "id119hr6517",
          "measure-number": "6517",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-09",
          "originChamber": "HOUSE",
          "update-date": "2026-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6517v00",
            "update-date": "2026-02-06"
          },
          "action-date": "2025-12-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill revises the procedures for appointing and removing the Librarian of Congress, the Director of the Government Publishing Office (GPO), and the Comptroller General by giving Congress the sole authority to appoint and remove these positions.</p><p>Specifically, the bill requires the Librarian and the Director of GPO to each be selected by a bipartisan congressional commission (as established by the bill) and appointed by Congress through the adoption of a concurrent resolution. (Currently, these positions are appointed by the President with the advice and consent of the Senate.) The Librarian and the Director of GPO may only be removed from office by an affirmative three-fifths vote in each chamber.</p><p>Additionally, the bill revises the appointment process for the Comptroller General. (Currently, the Comptroller General is appointed by the President with the advice and consent of the Senate. A bipartisan congressional commission recommends at least three individuals to the President, who may ask the commission to recommend additional individuals.) This bill instead requires the bipartisan congressional commission to recommend one individual to Congress, and Congress may ask the commission to recommend additional individuals.\u00a0Congress must then appoint the selected individual through the adoption of a concurrent resolution.\u00a0</p><p>Further, the bill revises the removal process for the Comptroller General. (Currently, the Comptroller General may be removed from office by impeachment or by joint resolution of Congress.) This bill changes the removal process so the individual may only be removed by impeachment or by concurrent (instead of joint) resolution of Congress.</p>"
        },
        "title": "To modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6517.xml",
    "summary": {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill revises the procedures for appointing and removing the Librarian of Congress, the Director of the Government Publishing Office (GPO), and the Comptroller General by giving Congress the sole authority to appoint and remove these positions.</p><p>Specifically, the bill requires the Librarian and the Director of GPO to each be selected by a bipartisan congressional commission (as established by the bill) and appointed by Congress through the adoption of a concurrent resolution. (Currently, these positions are appointed by the President with the advice and consent of the Senate.) The Librarian and the Director of GPO may only be removed from office by an affirmative three-fifths vote in each chamber.</p><p>Additionally, the bill revises the appointment process for the Comptroller General. (Currently, the Comptroller General is appointed by the President with the advice and consent of the Senate. A bipartisan congressional commission recommends at least three individuals to the President, who may ask the commission to recommend additional individuals.) This bill instead requires the bipartisan congressional commission to recommend one individual to Congress, and Congress may ask the commission to recommend additional individuals.\u00a0Congress must then appoint the selected individual through the adoption of a concurrent resolution.\u00a0</p><p>Further, the bill revises the removal process for the Comptroller General. (Currently, the Comptroller General may be removed from office by impeachment or by joint resolution of Congress.) This bill changes the removal process so the individual may only be removed by impeachment or by concurrent (instead of joint) resolution of Congress.</p>",
      "updateDate": "2026-02-06",
      "versionCode": "id119hr6517"
    },
    "title": "To modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-12-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill revises the procedures for appointing and removing the Librarian of Congress, the Director of the Government Publishing Office (GPO), and the Comptroller General by giving Congress the sole authority to appoint and remove these positions.</p><p>Specifically, the bill requires the Librarian and the Director of GPO to each be selected by a bipartisan congressional commission (as established by the bill) and appointed by Congress through the adoption of a concurrent resolution. (Currently, these positions are appointed by the President with the advice and consent of the Senate.) The Librarian and the Director of GPO may only be removed from office by an affirmative three-fifths vote in each chamber.</p><p>Additionally, the bill revises the appointment process for the Comptroller General. (Currently, the Comptroller General is appointed by the President with the advice and consent of the Senate. A bipartisan congressional commission recommends at least three individuals to the President, who may ask the commission to recommend additional individuals.) This bill instead requires the bipartisan congressional commission to recommend one individual to Congress, and Congress may ask the commission to recommend additional individuals.\u00a0Congress must then appoint the selected individual through the adoption of a concurrent resolution.\u00a0</p><p>Further, the bill revises the removal process for the Comptroller General. (Currently, the Comptroller General may be removed from office by impeachment or by joint resolution of Congress.) This bill changes the removal process so the individual may only be removed by impeachment or by concurrent (instead of joint) resolution of Congress.</p>",
      "updateDate": "2026-02-06",
      "versionCode": "id119hr6517"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6517ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:33Z"
    },
    {
      "title": "To modify the appointment process for the Librarian of Congress, the Comptroller General, and the Director of the Government Publishing Office, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T09:05:53Z"
    }
  ]
}
```
