# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7886
- Title: Failed Bank Executives Accountability and Consequences Act
- Congress: 119
- Bill type: HR
- Bill number: 7886
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7886",
    "number": "7886",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Failed Bank Executives Accountability and Consequences Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7886ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7886\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Ms. Waters introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide Federal financial regulators with clawback authority over executive compensation and additional industry prohibition and civil money penalty authority with respect to executives whose negligence caused financial loss to the applicable financial institution, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Failed Bank Executives Accountability and Consequences Act .\n#### 2. Sense of Congress\nIt is the sense of the Congress that\u2014\n**(1)**\nfinancial regulators and law enforcement agencies should fully exercise the maximum extent of their authorities to investigate and use available enforcement tools to hold executive officers and board members at Silicon Valley Bank, Signature Bank, First Republic Bank, and any other bank that fails to be fully accountable for any misconduct in which they are found to have engaged; and\n**(2)**\nthe Board of Governors of the Federal Reserve System, the Office of the Comptroller of the Currency, the Board of Directors of the Federal Deposit Insurance Corporation, the National Credit Union Administration Board, the Securities and Exchange Commission, the Federal Housing Finance Agency should jointly finalize the regulations or guidelines required under section 956 of the Investor Protection and Securities Reform Act of 2010 , and those regulations or guidelines should include robust clawback requirements.\n#### 3. Clawback authority\n##### (a) In general\nSection 8 of the Federal Deposit Insurance Act ( 12 U.S.C. 1818 ) is amended by adding at the end the following:\n(x) Recoupment of compensation from executive officers and directors (1) In general During any period in which the Corporation is acting as conservator or receiver for an insured depository institution, the Corporation may recover, from any current or former executive officer or director of such insured depository institution whose negligence caused financial loss to such insured depository institution, any compensation received during the 2-year period preceding the date on which the Corporation was appointed as the conservator or receiver of the insured depository institution, except that, in the case of fraud, no time limit shall apply. (2) Rulemaking The Corporation shall promulgate regulations to implement the requirements of this subsection, including defining the term compensation to mean any financial remuneration, including salary, bonuses, incentives, benefits, severance, deferred compensation, or golden parachute benefits, and any profits realized from the sale of the securities of the insured depository institution (or the securities of an affiliate of the insured depository institution). .\n##### (b) Clawback authority relating to orderly liquidation authority\nSection 210(s)(1) of the Dodd-Frank Wall Street Reform and Consumer Protection Act is amended to read as follows:\n(1) In general The Corporation, as receiver of a covered financial company, may recover from any current or former executive officer or director whose negligence caused financial loss to the covered financial company any compensation received during the 2-year period preceding the date on which the Corporation was appointed as the receiver of the covered financial company, except that, in the case of fraud, no time limit shall apply. .\n#### 4. Removal and prohibition authority in the case of institution failure\n##### (a) In general\nSection 8(e) of the Federal Deposit Insurance Act ( 12 U.S.C. 1818(e) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (3), (4), (5), (6), and (7) as paragraphs (4), (5), (6), (7), and (8), respectively; and\n**(2)**\nby inserting after paragraph (2) the following:\n(3) Suspension, removal, and prohibition from participation orders in the case of institution failure Whenever the appropriate Federal banking agency determines that an institution-affiliated party has negligently caused financial loss to any insured depository institution that has failed, the appropriate Federal banking agency for the depository institution may serve upon such party a written notice of the agency\u2019s intention to prohibit any further participation by such party, in any manner, in the conduct of the affairs of any insured depository institution. .\n##### (b) Conforming amendment\nThe Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ) is amended\u2014\n**(1)**\nin section 8\u2014\n**(A)**\nin subsection (e)\u2014\n**(i)**\nin paragraph (3), by striking under paragraph (1) or (2) each place it occurs and inserting under paragraphs (1), (2), or (3) ; and\n**(ii)**\nin paragraph (7), as so redesignated, by striking paragraph (7)(A) and inserting paragraph (8)(A) ;\n**(B)**\nin subsection (f), by striking subsection (e)(3) and inserting subsection (e)(4) ;\n**(C)**\nin subsection (g)(1)(D)(ii), by striking paragraph (1), (2), or (3) of subsection (e) and inserting paragraph (1), (2), or (4) of subsection (e) ; and\n**(D)**\nin subsection (j), by striking subsection (e)(6) and inserting subsection (e)(7) ; and\n**(2)**\nin section 10(k)(6)\u2014\n**(A)**\nin subparagraph (A)(i), by striking section 8(e)(4) for written notices or orders under paragraph (1) or (2) of section 8(e) and inserting section 8(e)(5) for written notices or orders under paragraph (1), (2), or (3) of section 8(e) ; and\n**(B)**\nin subparagraph (B), by striking paragraphs (6) and (7) of section 8(e) and inserting paragraphs (7) and (8) of section 8(e) .\n#### 5. Fines for failed bank executives\n##### (a) In general\nSection 8(i)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1818(i)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (D), (E), (F), (G), (H), (I), (J), and (K) as paragraphs (E), (F), (G), (H), (I), (J), (K), and (L), respectively; and\n**(2)**\nby inserting after subparagraph (C), the following:\n(D) Fines for contributing to institution failure (i) First tier Notwithstanding subparagraphs (A), (B), and (C), any executive officer or director who has negligently caused financial loss to any insured depository institution that has failed shall forfeit and pay a civil penalty of not more than $25,000 for each day during which such conduct occurred. (ii) Second tier Notwithstanding subparagraphs (A), (B), and (C), any executive officer or director who knowingly or recklessly caused financial loss to any insured depository institution that has failed shall forfeit and pay a civil penalty in an amount not to exceed the applicable maximum amount determined under subparagraph (E) for each day during which such conduct occurred. .\n##### (b) Conforming amendments\nSection 8(i)(2) of the Federal Deposit Insurance Act ( 12 U.S.C. 1818(i)(2) ), as amended by subsection (a) is further amended\u2014\n**(1)**\nin subparagraph (E), by striking to subparagraph (C) and inserting to subparagraph (C) or (D) ;\n**(2)**\nin subparagraph (F)\u2014\n**(A)**\nby striking under subparagraph (A), (B), or (C) and inserting under subparagraph (A), (B), (C), or (D) ; and\n**(B)**\nby striking subparagraph (H) and inserting subparagraph (I) ;\n**(3)**\nin subparagraph (G), by striking under subparagraph (A), (B), or (C) and inserting under subparagraph (A), (B), (C), or (D) ; and\n**(4)**\nin subparagraph (H), by striking under subparagraph (A), (B), or (C) and inserting under subparagraph (A), (B), (C), or (D) .\n#### 6. Rule of construction\nThis Act and the amendments made by this Act may not be construed to limit the enforcement authorities that financial regulators and law enforcement agencies had, prior to the date of enactment of this Act, to hold executive officers and board members of insured depository institutions and covered financial companies accountable for any misconduct in which they are found to have engaged.",
      "versionDate": "2026-03-09",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-21T16:06:36Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7886ih.xml"
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
      "title": "Failed Bank Executives Accountability and Consequences Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Failed Bank Executives Accountability and Consequences Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide Federal financial regulators with clawback authority over executive compensation and additional industry prohibition and civil money penalty authority with respect to executives whose negligence caused financial loss to the applicable financial institution, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:33:35Z"
    }
  ]
}
```
