# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1333
- Title: Strengthening Child Exploitation Enforcement Act
- Congress: 119
- Bill type: S
- Bill number: 1333
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2026-03-24T19:35:52Z
- Update date including text: 2026-03-24T19:35:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-09-29 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S6843-6844)
- 2025-09-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-09-29 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-09-29 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S6843-6844)
- 2025-10-08 - Floor: Message on Senate action sent to the House.
- 2025-10-10 12:33:04 - Floor: Received in the House.
- 2025-10-10 12:33:05 - Floor: Held at the desk.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-09-29 - Floor: Passed Senate without amendment by Unanimous Consent. (text: CR S6843-6844)
- 2025-09-29 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-09-29 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-09-29 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S6843-6844)
- 2025-10-08 - Floor: Message on Senate action sent to the House.
- 2025-10-10 12:33:04 - Floor: Received in the House.
- 2025-10-10 12:33:05 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1333",
    "number": "1333",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Strengthening Child Exploitation Enforcement Act",
    "type": "S",
    "updateDate": "2026-03-24T19:35:52Z",
    "updateDateIncludingText": "2026-03-24T19:35:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-10-10",
      "actionTime": "12:33:05",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-10-10",
      "actionTime": "12:33:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (text: CR S6843-6844)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent. (consideration: CR S6843-6844)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-08",
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
            "date": "2025-09-30T01:49:10Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-04-08T16:46:19Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1333is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1333\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Cornyn (for himself and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to modify provisions relating to kidnapping, sexual abuse, and illicit sexual conduct with respect to minors.\n#### 1. Short title\nThis Act may be cited as the Strengthening Child Exploitation Enforcement Act .\n#### 2. Kidnapping; sexual abuse; illicit sexual conduct with respect to minors\n##### (a) In general\nPart I of title 18, United States Code, is amended\u2014\n**(1)**\nin section 1201\u2014\n**(A)**\nin subsection (a), in the matter preceding paragraph (1), by inserting obtains by defrauding or deceiving any person, after abducts, ;\n**(B)**\nin subsection (b), by inserting obtained by defrauding or deceiving any person, after abducted, ; and\n**(C)**\nin subsection (g), by adding at the end the following:\n(2) Defense For an offense described in this subsection involving a victim who has not attained the age of 16 years, it is not a defense that the victim consented to the conduct of the offender, unless the offender can establish by a preponderance of the evidence that the offender reasonably believed that the victim had attained the age of 16 years. ;\n**(2)**\nin chapter 109A\u2014\n**(A)**\nin section 2241(c), by striking crosses a State line and inserting travels in interstate or foreign commerce ;\n**(B)**\nin section 2242(3), by striking , to include doing so and inserting or ;\n**(C)**\nin section 2243, by adding at the end the following:\n(f) Intentional touching involving individuals under the age of 16 (1) Offense It shall be unlawful, in the special maritime and territorial jurisdiction of the United States or in a Federal prison, or in any prison, institution, or facility in which persons are held in custody by direction of or pursuant to a contract or agreement with the head of any Federal department or agency, to knowingly cause the intentional touching, not through the clothing, of the genitalia of any person by a person who has not attained the age of 16 years, with an intent to abuse, humiliate, harass, degrade, or arouse or gratify the sexual desire of any person, or attempt to do so, if to do so would violate subsection (a), (b), or (c) of this section, section 2241, or section 2242 had such intentional touching been a sexual act. (2) Penalty Any person who violates paragraph (1) shall be fined under this title, imprisoned as provided in the applicable provision of law described in that paragraph, or both. ; and\n**(D)**\nin section 2244\u2014\n**(i)**\nin subsection (a)\u2014\n**(I)**\nby redesignating paragraphs (1) through (6) as subparagraphs (A) through (F), respectively, and adjusting the margins accordingly;\n**(II)**\nby striking Whoever and inserting the following:\n(1) In general Whoever ;\n**(III)**\nin paragraph (1), as so designated\u2014\n**(aa)**\nin the matter preceding subparagraph (A), as so redesignated, by striking if so to do and inserting if to do so ;\n**(bb)**\nin subparagraph (A), as so redesignated, by striking ten and inserting 10 ;\n**(cc)**\nin subparagraph (B), as so redesignated, by striking three and inserting 3 ;\n**(dd)**\nin subparagraph (C), as so redesignated, by striking two and inserting 2 ;\n**(ee)**\nin subparagraph (D), as so redesignated, by striking two and inserting 2 ; and\n**(ff)**\nin subparagraph (F), as so redesignated, by striking the semicolon at the end and inserting a period; and\n**(IV)**\nby adding at the end the following:\n(2) Attempt Whoever attempts to commit an offense under paragraph (1) shall be subject to the same penalty as for a completed offense. ;\n**(ii)**\nin subsection (b)\u2014\n**(I)**\nby inserting or causes after engages in ;\n**(II)**\nby inserting or by after sexual contact with ;\n**(III)**\nby inserting , or attempts to do so, after other person\u2019s permission ; and\n**(IV)**\nby striking two and inserting 2 ; and\n**(iii)**\nin subsection (c), by striking If the sexual contact that violates this section (other than subsection (a)(5)) is with an individual and inserting If the sexual contact or attempted sexual contact that a person engages in or causes in violation of this section (other than subsection (a)(1)(E)) is with or by an individual ; and\n**(3)**\nin section 2423(g)(1)\u2014\n**(A)**\nby striking a sexual act (as defined in section 2246) with and inserting any conduct involving ; and\n**(B)**\nby striking sexual act occurred and inserting conduct occurred .\n##### (b) Effective date\nThe amendment to section 2241(c) of title 18, United States Code, made by subsection (a) shall apply to conduct that occurred before, on, or after the date of enactment of this Act.\n#### 3. Conforming amendments relating to abusive sexual contact\n##### (a) Penalties for civil rights offenses involving sexual misconduct\nSection 250(b) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking section 2244(a)(5), and inserting section 2244(a)(1)(E), or an attempt to engage in or cause such contact as prohibited by section 2244(a)(2), ;\n**(2)**\nin paragraph (4), in the matter preceding subparagraph (A), by striking subsection (a)(1) or (b) of section 2244, but excluding abusive sexual contact through the clothing and inserting section 2244(a)(1)(A), an attempt to engage in or cause such contact as prohibited by section 2244(a)(2), or abusive sexual contact of the type prohibited by section 2244(b), but excluding abusive sexual contact through the clothing or an attempt to engage in or cause such contact ;\n**(3)**\nin paragraph (5), in the matter preceding subparagraph (A), by striking section 2244(a)(2) and inserting section 2244(a)(1)(B) or an attempt to engage in or cause such contact as prohibited by section 2244(a)(2) ; and\n**(4)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking subsection (a)(3), (a)(4), or (b) of section 2244 and inserting subparagraph (C) or (D) of section 2244(a)(1), an attempt to engage in or cause such contact as prohibited by section 2244(a)(2), or abusive sexual contact of the type prohibited by section 2244(b) .\n##### (b) Sentencing classification of offenses\nSection 3559 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(2)(F)(i), by striking sections 2244(a)(1) and (a)(2) and inserting subparagraphs (A) and (B) of section 2244(a)(1) ; and\n**(2)**\nin subsection (e)(2)(A), by striking 2244(a)(1) and inserting 2244(a)(1)(A) .",
      "versionDate": "2025-04-08",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1333es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1333\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend title 18, United States Code, to modify provisions relating to kidnapping, sexual abuse, and illicit sexual conduct with respect to minors.\n#### 1. Short title\nThis Act may be cited as the Strengthening Child Exploitation Enforcement Act .\n#### 2. Kidnapping; sexual abuse; illicit sexual conduct with respect to minors\n##### (a) In general\nPart I of title 18, United States Code, is amended\u2014\n**(1)**\nin section 1201\u2014\n**(A)**\nin subsection (a), in the matter preceding paragraph (1), by inserting obtains by defrauding or deceiving any person, after abducts, ;\n**(B)**\nin subsection (b), by inserting obtained by defrauding or deceiving any person, after abducted, ; and\n**(C)**\nin subsection (g), by adding at the end the following:\n(2) Defense For an offense described in this subsection involving a victim who has not attained the age of 16 years, it is not a defense that the victim consented to the conduct of the offender, unless the offender can establish by a preponderance of the evidence that the offender reasonably believed that the victim had attained the age of 16 years. ;\n**(2)**\nin chapter 109A\u2014\n**(A)**\nin section 2241(c), by striking crosses a State line and inserting travels in interstate or foreign commerce ;\n**(B)**\nin section 2242(3), by striking , to include doing so and inserting or ;\n**(C)**\nin section 2243, by adding at the end the following:\n(f) Intentional touching involving individuals under the age of 16 (1) Offense It shall be unlawful, in the special maritime and territorial jurisdiction of the United States or in a Federal prison, or in any prison, institution, or facility in which persons are held in custody by direction of or pursuant to a contract or agreement with the head of any Federal department or agency, to knowingly cause the intentional touching, not through the clothing, of the genitalia of any person by a person who has not attained the age of 16 years, with an intent to abuse, humiliate, harass, degrade, or arouse or gratify the sexual desire of any person, or attempt to do so, if to do so would violate subsection (a), (b), or (c) of this section, section 2241, or section 2242 had such intentional touching been a sexual act. (2) Penalty Any person who violates paragraph (1) shall be fined under this title, imprisoned as provided in the applicable provision of law described in that paragraph, or both. ; and\n**(D)**\nin section 2244\u2014\n**(i)**\nin subsection (a)\u2014\n**(I)**\nby redesignating paragraphs (1) through (6) as subparagraphs (A) through (F), respectively, and adjusting the margins accordingly;\n**(II)**\nby striking Whoever and inserting the following:\n(1) In general Whoever ;\n**(III)**\nin paragraph (1), as so designated\u2014\n**(aa)**\nin the matter preceding subparagraph (A), as so redesignated, by striking if so to do and inserting if to do so ;\n**(bb)**\nin subparagraph (A), as so redesignated, by striking ten and inserting 10 ;\n**(cc)**\nin subparagraph (B), as so redesignated, by striking three and inserting 3 ;\n**(dd)**\nin subparagraph (C), as so redesignated, by striking two and inserting 2 ;\n**(ee)**\nin subparagraph (D), as so redesignated, by striking two and inserting 2 ; and\n**(ff)**\nin subparagraph (F), as so redesignated, by striking the semicolon at the end and inserting a period; and\n**(IV)**\nby adding at the end the following:\n(2) Attempt Whoever attempts to commit an offense under paragraph (1) shall be subject to the same penalty as for a completed offense. ;\n**(ii)**\nin subsection (b)\u2014\n**(I)**\nby inserting or causes after engages in ;\n**(II)**\nby inserting or by after sexual contact with ;\n**(III)**\nby inserting , or attempts to do so, after other person\u2019s permission ; and\n**(IV)**\nby striking two and inserting 2 ; and\n**(iii)**\nin subsection (c), by striking If the sexual contact that violates this section (other than subsection (a)(5)) is with an individual and inserting If the sexual contact or attempted sexual contact that a person engages in or causes in violation of this section (other than subsection (a)(1)(E)) is with or by an individual ; and\n**(3)**\nin section 2423(g)(1)\u2014\n**(A)**\nby striking a sexual act (as defined in section 2246) with and inserting any conduct involving ; and\n**(B)**\nby striking sexual act occurred and inserting conduct occurred .\n##### (b) Effective date\nThe amendment to section 2241(c) of title 18, United States Code, made by subsection (a) shall apply to conduct that occurred before, on, or after the date of enactment of this Act.\n#### 3. Conforming amendments relating to abusive sexual contact\n##### (a) Penalties for civil rights offenses involving sexual misconduct\nSection 250(b) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (2), by striking section 2244(a)(5), and inserting section 2244(a)(1)(E), or an attempt to engage in or cause such contact as prohibited by section 2244(a)(2), ;\n**(2)**\nin paragraph (4), in the matter preceding subparagraph (A), by striking subsection (a)(1) or (b) of section 2244, but excluding abusive sexual contact through the clothing and inserting section 2244(a)(1)(A), an attempt to engage in or cause such contact as prohibited by section 2244(a)(2), or abusive sexual contact of the type prohibited by section 2244(b), but excluding abusive sexual contact through the clothing or an attempt to engage in or cause such contact ;\n**(3)**\nin paragraph (5), in the matter preceding subparagraph (A), by striking section 2244(a)(2) and inserting section 2244(a)(1)(B) or an attempt to engage in or cause such contact as prohibited by section 2244(a)(2) ; and\n**(4)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking subsection (a)(3), (a)(4), or (b) of section 2244 and inserting subparagraph (C) or (D) of section 2244(a)(1), an attempt to engage in or cause such contact as prohibited by section 2244(a)(2), or abusive sexual contact of the type prohibited by section 2244(b) .\n##### (b) Sentencing classification of offenses\nSection 3559 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(2)(F)(i), by striking sections 2244(a)(1) and (a)(2) and inserting subparagraphs (A) and (B) of section 2244(a)(1) ; and\n**(2)**\nin subsection (e)(2)(A), by striking 2244(a)(1) and inserting 2244(a)(1)(A) .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-04-08",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "2735",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Strengthening Child Exploitation Enforcement Act",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-09-30T18:01:01Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-09-30T18:01:01Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-09-30T18:01:01Z"
          },
          {
            "name": "Domestic violence and child abuse",
            "updateDate": "2025-09-30T18:01:01Z"
          },
          {
            "name": "Sex offenses",
            "updateDate": "2025-09-30T18:01:01Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-09-30T18:01:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-23T16:53:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-29",
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
          "measure-id": "id119s1333",
          "measure-number": "1333",
          "measure-type": "s",
          "orig-publish-date": "2025-09-29",
          "originChamber": "SENATE",
          "update-date": "2026-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1333v55",
            "update-date": "2026-03-24"
          },
          "action-date": "2025-09-29",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Strengthening Child Exploitation Enforcement Act</strong></p><p>This bill makes changes to federal criminal laws related to various offenses, particularly sexual abuse offenses against minors.</p><p>The bill revises the federal kidnapping statute by specifying that obtaining a victim by defrauding or deceiving a third party constitutes the offense of kidnapping.\u00a0Additionally, for a kidnapping offense that involves a victim who has not attained the age of 16, the bill specifies that it is not a defense that the victim consented to the conduct of the offender, unless the offender establishes by a preponderance of the evidence that the offender reasonably believed that the victim had attained the age of 16.</p><p>The bill also revises statutes related to sexual abuse offenses against minors to specify the following:</p><ul><li>that crossing international lines with the intent to engage in a sexual act with a child who has not attained the age of 12 constitutes aggravated sexual abuse (currently, the statute only references crossing state lines),</li><li>that the offense of sexual abuse of a minor also includes knowingly causing the intentional touching of any person by a person who has not attained the age of 16, and</li><li>that attempting to commit abusive sexual contact is also a crime that is subject to the same penalty as the completed offense.</li></ul>"
        },
        "title": "Strengthening Child Exploitation Enforcement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1333.xml",
    "summary": {
      "actionDate": "2025-09-29",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Strengthening Child Exploitation Enforcement Act</strong></p><p>This bill makes changes to federal criminal laws related to various offenses, particularly sexual abuse offenses against minors.</p><p>The bill revises the federal kidnapping statute by specifying that obtaining a victim by defrauding or deceiving a third party constitutes the offense of kidnapping.\u00a0Additionally, for a kidnapping offense that involves a victim who has not attained the age of 16, the bill specifies that it is not a defense that the victim consented to the conduct of the offender, unless the offender establishes by a preponderance of the evidence that the offender reasonably believed that the victim had attained the age of 16.</p><p>The bill also revises statutes related to sexual abuse offenses against minors to specify the following:</p><ul><li>that crossing international lines with the intent to engage in a sexual act with a child who has not attained the age of 12 constitutes aggravated sexual abuse (currently, the statute only references crossing state lines),</li><li>that the offense of sexual abuse of a minor also includes knowingly causing the intentional touching of any person by a person who has not attained the age of 16, and</li><li>that attempting to commit abusive sexual contact is also a crime that is subject to the same penalty as the completed offense.</li></ul>",
      "updateDate": "2026-03-24",
      "versionCode": "id119s1333"
    },
    "title": "Strengthening Child Exploitation Enforcement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-29",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Strengthening Child Exploitation Enforcement Act</strong></p><p>This bill makes changes to federal criminal laws related to various offenses, particularly sexual abuse offenses against minors.</p><p>The bill revises the federal kidnapping statute by specifying that obtaining a victim by defrauding or deceiving a third party constitutes the offense of kidnapping.\u00a0Additionally, for a kidnapping offense that involves a victim who has not attained the age of 16, the bill specifies that it is not a defense that the victim consented to the conduct of the offender, unless the offender establishes by a preponderance of the evidence that the offender reasonably believed that the victim had attained the age of 16.</p><p>The bill also revises statutes related to sexual abuse offenses against minors to specify the following:</p><ul><li>that crossing international lines with the intent to engage in a sexual act with a child who has not attained the age of 12 constitutes aggravated sexual abuse (currently, the statute only references crossing state lines),</li><li>that the offense of sexual abuse of a minor also includes knowingly causing the intentional touching of any person by a person who has not attained the age of 16, and</li><li>that attempting to commit abusive sexual contact is also a crime that is subject to the same penalty as the completed offense.</li></ul>",
      "updateDate": "2026-03-24",
      "versionCode": "id119s1333"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1333is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1333es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Strengthening Child Exploitation Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T11:03:14Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Strengthening Child Exploitation Enforcement Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-09-30T07:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Child Exploitation Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-22T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to modify provisions relating to kidnapping, sexual abuse, and illicit sexual conduct with respect to minors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-22T03:48:32Z"
    }
  ]
}
```
