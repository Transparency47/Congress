# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1620
- Title: MEME Act
- Congress: 119
- Bill type: S
- Bill number: 1620
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2026-02-25T20:28:44Z
- Update date including text: 2026-02-25T20:28:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1620",
    "number": "1620",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "MEME Act",
    "type": "S",
    "updateDate": "2026-02-25T20:28:44Z",
    "updateDateIncludingText": "2026-02-25T20:28:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T18:53:12Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1620is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1620\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Murphy introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend chapter 131 of title 5, United States Code, with respect to prohibited financial transactions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modern Emoluments and Malfeasance Enforcement Act or the MEME Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nfederally elected officials must not utilize those positions, granted by the trust of the public, for private financial gain;\n**(2)**\nthe issuance, sponsorship, or promotion of financial instruments by public office holders deprives the public of the honest services of the public office holders, facilitates bribery by investors or purchasers, and results in public exploitation and corrupt foreign influence; and\n**(3)**\nMembers of Congress and the executive branch must not seek to use public office to benefit financially, but rather those positions should be held in trust for the benefit of the public in the United States.\n#### 3. Prohibited financial transactions\n##### (a) Financial exploitation by public office holders\n**(1) In general**\nChapter 131 of title 5, United States Code, is amended by adding at the end the following:\nIV Financial exploitation by public office holders 13151. Definitions In this subchapter: (1) Adjacent individual The term adjacent individual means\u2014 (A) each officer or employee in the executive branch holding a Senior Executive Service position (as defined in section 3132(a)(2)); (B) each member of a uniformed service whose pay grade is at or in excess of O\u20137 under section 201 of title 37; (C) each officer or employee in any other position in the executive branch determined by the Office of the Special Counsel, in consultation with the Director of the Office of Government Ethics, to be of equal classification to a position described in subparagraph (A) or (B); or (D) the spouse or dependent child of any individual described in subparagraph (A), (B), or (C). (2) Covered asset The term covered asset means\u2014 (A) a security (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (B) a security future (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (C) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); (D) a digital asset that can be sold for remuneration, including a cryptocurrency, a meme coin, a token, or a non-fungible token; or (E) any derivative, option, warrant, mutual fund, or exchange-traded fund of an asset described in subparagraphs (A) through (D). (3) Covered individual The term covered individual means\u2014 (A) the President; (B) the Vice President; (C) a public official (as defined in section 201(a) of title 18); or (D) the spouse or dependent child of any individual described in subparagraph (A), (B), or (C). (4) Dependent child The term dependent child has the meaning given the term in section 13101. (5) Prohibited financial transaction The term prohibited financial transaction means the issuance, sponsorship, or promotion of a covered asset for pecuniary gain. 13152. Prohibition on certain transactions (a) Prohibition Except as provided in subsection (b), a covered individual or an adjacent individual may not engage in or benefit from a prohibited financial transaction\u2014 (1) during the term of service of the covered individual or adjacent individual; (2) during the 180-day period ending on the date on which the service of the covered individual or adjacent individual commences; or (3) during the 180-day period beginning on the date on which the service of the covered individual or adjacent individual is terminated. (b) Adjacent individuals With respect to adjacent individuals, nothing in this section shall be construed to limit the application of section 208 of title 18. (c) Liability and immunity For purposes of any immunities to civil liability, any conduct comprising or relating to a prohibited financial transaction under this section shall be deemed an unofficial act and beyond the scope of the official duties of the relevant covered individual or adjacent individual. 13153. Civil penalties (a) Civil action The Attorney General may bring a civil action in any appropriate district court of the United States against any covered individual or adjacent individual who violates section 13152(a). (b) Civil penalty Any covered individual or adjacent individual who knowingly violates section 13152(a) shall be subject to a civil monetary penalty of not more than $250,000. (c) Disgorgement A covered individual or an adjacent individual who is found to have violated section 13152(a) in a civil action under subsection (a) of this section shall disgorge to the Treasury of the United States any profit from the unlawful activity that is the subject of that civil action. .\n**(2) Clerical amendment**\nThe table of sections for chapter 131 of title 5, United States Code, is amended by adding at the end the following:\nSUBCHAPTER IV\u2014Financial exploitation by public office holders 13151. Definitions. 13152. Prohibition on certain transactions. 13153. Civil penalties. .\n##### (b) Criminal penalties\n**(1) Prohibited financial transactions**\nChapter 11 of title 18, United States is amended by inserting after section 220 the following:\n221. Prohibited financial transactions (a) Definitions In this section: (1) Adjacent individual The term adjacent individual means\u2014 (A) each officer or employee in the executive branch holding a Senior Executive Service position (as defined in section 3132(a)(2) of title 5); (B) each member of a uniformed service whose pay grade is at or in excess of O\u20137 under section 201 of title 37; (C) each officer or employee in any other position in the executive branch determined by the Office of the Special Counsel, in consultation with the Director of the Office of Government Ethics, to be of equal classification to a position described in subparagraph (A) or (B); or (D) the spouse or dependent child of any individual described in subparagraph (A), (B), or (C). (2) Covered asset The term covered asset means\u2014 (A) a security (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (B) a security future (as defined in section 3(a) of Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) )); (C) a commodity (as defined in section 1a of the Commodity Exchange Act ( 7 U.S.C. 1a )); (D) a digital asset that can be sold for remuneration, including a cryptocurrency, a meme coin, a token, or a non-fungible token; or (E) any derivative, option, warrant, mutual fund, or exchange-traded fund of an asset described in subparagraphs (A) through (D). (3) Covered individual The term covered individual means\u2014 (A) the President; (B) the Vice President; (C) a public official (as defined in section 201(a)); or (D) the spouse or dependent child of any individual described in subparagraph (A), (B), or (C). (4) Dependent child The term dependent child has the meaning given the term in section 13101 of title 5. (5) Prohibited financial transaction The term prohibited financial transaction means the issuance, sponsorship, or promotion of a covered asset for pecuniary gain. (b) Benefit from prohibited financial transaction Any covered individual or adjacent individual who\u2014 (1) knowingly violates any provision of section 13152(a) of title 5; and (2) through such violation\u2014 (A) causes an aggregate loss of not less than $1,000,000 to 1 or more persons in the United States; or (B) benefits financially, through profit, gain, or advantage, directly or indirectly through any family member or business associate of the covered individual or adjacent individual, from the sale, purchase, or distribution of the covered asset issued in violation of section 13152(a) of title 5, shall be fined under this title or imprisoned for not more than 5 years, or both. (c) Bribery Any covered individual or adjacent individual who\u2014 (1) knowingly violates any provision of section 13152(a) of title 5; and (2) directly or indirectly, corruptly demands, seeks, receives, accepts, or agrees to receive or accept any thing of value personally or for any other person or entity, in return for\u2014 (A) being influenced in the performance of any official act; (B) being influenced to commit or aid in committing, or to collude in, or allow, any fraud, or make opportunity for the commission of any fraud, on the United States; or (C) being induced to do or omit to do any act in violation of the official duty of such official or person, shall be fined under this title or not more than 3 times the amount of financial gain, if any, that the individual benefitted from relating to the prohibited conduct, whichever is greater, or imprisoned for not more than 15 years, or both, and may be disqualified from holding any office of honor, trust, or profit under the United States. (d) Insider trading Any covered individual or adjacent individual who knowingly violates section 13152(a) of title 5 and, in committing such violation, knowingly violates section 10(b) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78j(b) ), shall be fined under this title or not more than 3 times the amount of financial gain, if any, that the individual benefitted from relating to the prohibited conduct, whichever is greater, or imprisoned for not more than 15 years, or both, and may be disqualified from holding any office of honor, trust, or profit under the United States. (e) Liability and immunity For purposes of any immunities to civil and criminal liability, any conduct comprising or relating to a prohibited financial transaction under this section shall be deemed an unofficial act and beyond the scope of the official duties of the relevant covered individual or adjacent individual. .\n**(2) Clerical amendment**\nThe table of sections for chapter 11 of title 18, United States Code, is amended by inserting after the item relating to section 220 the following:\n221. Prohibited financial transactions. .",
      "versionDate": "2025-05-06",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-27T14:43:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
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
          "measure-id": "id119s1620",
          "measure-number": "1620",
          "measure-type": "s",
          "orig-publish-date": "2025-05-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1620v00",
            "update-date": "2026-02-25"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Modern Emoluments and Malfeasance Enforcement Act or the MEME Act</strong></p><p>This bill prohibits the President, the Vice\u00a0President, Members of Congress, those holding Senior Executive Service positions, admirals, generals, and other federal public officials from engaging in or benefiting from the issuance, sponsorship, or promotion of certain assets. The spouse and dependent children of such an official are also covered by the prohibition.</p><p>Assets covered by the bill are securities, security futures, commodities, digital assets such as cryptocurrency or a meme coin, as well as derivatives, options, warrants, mutual funds, or exchange traded funds of the preceding assets.</p><p>The prohibition applies to (1) such officials during their term of service and for 180\u00a0days prior to and after their service, and (2) the spouse and dependent children of such an official during that same period.</p><p>Civil and criminal penalties under the bill include disgorging (giving) to the Treasury any profits from prohibited transactions, fines, and imprisonment for up to five years. The bill provides additional penalties for such prohibited activities if they involve bribery or insider trading.</p><p>The U.S. Office of Special Counsel may also determine that federal employees or officers serving in other positions are covered by the prohibition.</p>"
        },
        "title": "MEME Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1620.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Modern Emoluments and Malfeasance Enforcement Act or the MEME Act</strong></p><p>This bill prohibits the President, the Vice\u00a0President, Members of Congress, those holding Senior Executive Service positions, admirals, generals, and other federal public officials from engaging in or benefiting from the issuance, sponsorship, or promotion of certain assets. The spouse and dependent children of such an official are also covered by the prohibition.</p><p>Assets covered by the bill are securities, security futures, commodities, digital assets such as cryptocurrency or a meme coin, as well as derivatives, options, warrants, mutual funds, or exchange traded funds of the preceding assets.</p><p>The prohibition applies to (1) such officials during their term of service and for 180\u00a0days prior to and after their service, and (2) the spouse and dependent children of such an official during that same period.</p><p>Civil and criminal penalties under the bill include disgorging (giving) to the Treasury any profits from prohibited transactions, fines, and imprisonment for up to five years. The bill provides additional penalties for such prohibited activities if they involve bribery or insider trading.</p><p>The U.S. Office of Special Counsel may also determine that federal employees or officers serving in other positions are covered by the prohibition.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s1620"
    },
    "title": "MEME Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Modern Emoluments and Malfeasance Enforcement Act or the MEME Act</strong></p><p>This bill prohibits the President, the Vice\u00a0President, Members of Congress, those holding Senior Executive Service positions, admirals, generals, and other federal public officials from engaging in or benefiting from the issuance, sponsorship, or promotion of certain assets. The spouse and dependent children of such an official are also covered by the prohibition.</p><p>Assets covered by the bill are securities, security futures, commodities, digital assets such as cryptocurrency or a meme coin, as well as derivatives, options, warrants, mutual funds, or exchange traded funds of the preceding assets.</p><p>The prohibition applies to (1) such officials during their term of service and for 180\u00a0days prior to and after their service, and (2) the spouse and dependent children of such an official during that same period.</p><p>Civil and criminal penalties under the bill include disgorging (giving) to the Treasury any profits from prohibited transactions, fines, and imprisonment for up to five years. The bill provides additional penalties for such prohibited activities if they involve bribery or insider trading.</p><p>The U.S. Office of Special Counsel may also determine that federal employees or officers serving in other positions are covered by the prohibition.</p>",
      "updateDate": "2026-02-25",
      "versionCode": "id119s1620"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1620is.xml"
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
      "title": "MEME Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MEME Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Modern Emoluments and Malfeasance Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend chapter 131 of title 5, United States Code, with respect to prohibited financial transactions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:25Z"
    }
  ]
}
```
