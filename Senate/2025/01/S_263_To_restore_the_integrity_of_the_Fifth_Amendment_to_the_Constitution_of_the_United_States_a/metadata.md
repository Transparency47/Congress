# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/263?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/263
- Title: FAIR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 263
- Origin chamber: Senate
- Introduced date: 2025-01-27
- Update date: 2026-04-21T15:40:40Z
- Update date including text: 2026-04-21T15:40:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-27: Introduced in Senate
- 2025-01-27 - IntroReferral: Introduced in Senate
- 2025-01-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-27: Introduced in Senate

## Actions

- 2025-01-27 - IntroReferral: Introduced in Senate
- 2025-01-27 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-27",
    "latestAction": {
      "actionDate": "2025-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/263",
    "number": "263",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "FAIR Act of 2025",
    "type": "S",
    "updateDate": "2026-04-21T15:40:40Z",
    "updateDateIncludingText": "2026-04-21T15:40:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-27",
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
      "actionDate": "2025-01-27",
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
          "date": "2025-01-27T22:47:18Z",
          "name": "Referred To"
        }
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
      "sponsorshipDate": "2025-01-27",
      "state": "NJ"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "UT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-27",
      "state": "ME"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "WY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s263is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 263\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2025 Mr. Paul (for himself, Mr. Booker , Mr. Lee , Mr. King , Mr. Crapo , Ms. Lummis , Mr. Wyden , Mr. Welch , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo restore the integrity of the Fifth Amendment to the Constitution of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fifth Amendment Integrity Restoration Act of 2025 or the FAIR Act of 2025 .\n#### 2. Civil forfeiture and nonjudicial forfeiture\nSection 983 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the subsection heading, by striking Claim; ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nin clause (i)\u2014\n**(aa)**\nby striking clauses (ii) through (v), in any nonjudicial and inserting clause (ii), in any ; and\n**(bb)**\nby striking 60 and inserting 7 ;\n**(II)**\nby striking clauses (ii) through (v); and\n**(III)**\nby inserting after clause (i) the following:\n(ii) If the identity or interest of a party is not determined until after the seizure or turnover but is determined before a declaration of forfeiture is entered, the Government shall determine the identity and address of the party or interest within 7 days after the seizure or turnover, and notice shall be sent to such interested party not later than 7 days after the determination by the Government of the identity and address of the party or the party\u2019s interest. ;\n**(ii)**\nby striking subparagraphs (B) and (C);\n**(iii)**\nby redesignating subparagraphs (D) through (F) as subparagraphs (B) through (D), respectively; and\n**(iv)**\nin subparagraph (C), as so redesignated, by striking nonjudicial ;\n**(C)**\nby striking paragraph (2);\n**(D)**\nby redesignating paragraphs (3) and (4) as paragraphs (2) and (3), respectively; and\n**(E)**\nin paragraph (2)(A), as so redesignated\u2014\n**(i)**\nby striking 90 and inserting 30 ; and\n**(ii)**\nby striking after a claim has been filed and inserting after the date of the seizure ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby amending subparagraph (A) to read as follows:\n(A) If a person with standing to contest the forfeiture of property in a civil forfeiture proceeding under a civil forfeiture statute is\u2014 (i) financially unable to obtain representation by counsel; or (ii) the cost of obtaining representation would exceed the value of the seized property, the court may authorize or appoint counsel to represent that person with respect to the claim. ; and\n**(ii)**\nin subparagraph (B), by inserting or appoint after authorize ; and\n**(B)**\nin paragraph (2)(A)\u2014\n**(i)**\nby striking in a judicial civil forfeiture proceeding and inserting in a civil forfeiture proceeding ;\n**(ii)**\nby inserting under paragraph (1) after counsel ;\n**(iii)**\nby striking , and the property subject to forfeiture is real property that is being used by the person as a primary residence, ; and\n**(iv)**\nby striking , at the request of the person, shall insure and inserting shall ensure ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1), by striking a preponderance of the evidence and inserting clear and convincing evidence ;\n**(B)**\nin paragraph (2), by striking a preponderance of the evidence and inserting clear and convincing evidence ; and\n**(C)**\nby striking paragraph (3) and inserting the following:\n(3) if the Government\u2019s theory of forfeiture is that the property was used to commit or facilitate the commission of a criminal offense, or was involved in the commission of a criminal offense, the Government shall establish, by clear and convincing evidence, that\u2014 (A) there was a substantial connection between the property and the offense; and (B) the owner of any interest in the seized property\u2014 (i) used the property with intent to facilitate the offense; or (ii) knowingly consented or was willfully blind to the use of the property by another in connection with the offense. ;\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking the second sentence and inserting the following: The Government shall have the burden of proving that the claimant is not an innocent owner by a preponderance of the evidence. ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking an owner who and all that follows through upon learning and inserting an owner who, upon learning ; and\n**(ii)**\nin subparagraph (B)(i), by inserting before For the purposes of this paragraph the following: If the Government satisfies its burden under paragraph (1), the claimant may rebut the Government\u2019s evidence related to his innocent ownership, including by showing that he did all that could reasonably be expected under the law. ;\n**(5)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (1), in the matter preceding subparagraph (A)\u2014\n**(i)**\nby striking nonjudicial ; and\n**(ii)**\nby striking a declaration and inserting an order ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking declaration and inserting order ; and\n**(ii)**\nby striking subparagraph (B) and inserting the following:\n(B) Any proceeding described in subparagraph (A) shall be commenced within 6 months of the entry of the order granting the motion. ; and\n**(C)**\nby striking paragraph (5);\n**(6)**\nin subsection (f)(1), in the matter preceding subparagraph (A), by striking (a) and inserting (a)(3)(A) ;\n**(7)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1), by striking (a)(4) and inserting (a)(3) ; and\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) In making this determination, the court shall consider such factors as\u2014 (A) the seriousness of the offense; (B) the extent of the nexus of the property to the offense; (C) the range of sentences available for the offense giving rise to forfeiture; (D) the fair market value of the property; and (E) the hardship to the property owner and dependents. ; and\n**(8)**\nby adding at the end the following:\n(k) (1) Notwithstanding any other provision of law\u2014 (A) no Federal seizing agency may conduct nonjudicial forfeitures; (B) no property may be subject to forfeiture except through judicial process; and (C) no order of forfeiture may be entered except by a United States district court. (2) In this subsection, the term nonjudicial forfeiture means an in rem action that permits the Federal seizing agency to start a forfeiture without judicial involvement. .\n#### 3. Disposition of forfeited property\n##### (a) Revisions to controlled substances act\nSection 511(e) of the Controlled Substances Act ( 21 U.S.C. 881(e) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking civilly or ;\n**(B)**\nby striking subparagraph (A); and\n**(C)**\nby redesignating subparagraphs (B) through (E) as subparagraphs (A) through (D), respectively;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i), by striking subparagraph (B) of paragraph (1) and inserting paragraph (1)(A) ; and\n**(B)**\nin subparagraph (B), by striking accordance with section 524(c) of title 28, and inserting the General Fund of the Treasury of the United States ;\n**(3)**\nby striking paragraph (3);\n**(4)**\nby redesignating paragraph (4) as paragraph (3); and\n**(5)**\nin paragraph (3), as redesignated\u2014\n**(A)**\nin subparagraph (A), by striking paragraph (1)(B) and inserting paragraph (1)(A) ; and\n**(B)**\nin subparagraph (B), in the matter preceding clause (i), by striking paragraph (1)(B) that is civilly or and inserting paragraph (1)(A) that is .\n##### (b) Revisions to title 18\nChapter 46 of title 18, United States Code, is amended\u2014\n**(1)**\nin section 981(e)\u2014\n**(A)**\nby striking is authorized and all that follows through or forfeiture of the property; and inserting shall forward to the Treasurer of the United States any proceeds of property forfeited pursuant to this section for deposit in the General Fund of the Treasury or transfer such property on such terms and conditions as such officer may determine\u2014 ;\n**(B)**\nby redesignating paragraphs (3), (4), (5), (6), and (7) as paragraphs (1), (2), (3), (4), and (5), respectively; and\n**(C)**\nin the matter following paragraph (5), as so redesignated\u2014\n**(i)**\nby striking the first, second, third, sixth, and eighth sentences; and\n**(ii)**\nby striking paragraph (3), (4), or (5) and inserting paragraph (1), (2), or (3) ; and\n**(2)**\nin section 983(g)\u2014\n**(A)**\nin paragraph (3), by striking grossly ; and\n**(B)**\nin paragraph (4), by striking grossly .\n##### (c) Tariff act of 1930\nThe Tariff Act of 1930 ( 19 U.S.C. 1304 et seq. ) is amended\u2014\n**(1)**\nin section 613A(a) ( 19 U.S.C. 1613b(a) )\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (D), by inserting and after the semicolon;\n**(ii)**\nin subparagraph (E), by striking ; and and inserting a period; and\n**(iii)**\nby striking subparagraph (F); and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking (A) Any payment and inserting Any payment ; and\n**(ii)**\nby striking subparagraph (B); and\n**(2)**\nin section 616 ( 19 U.S.C. 1616a )\u2014\n**(A)**\nin the section heading, by striking TRANSFER OF FORFEITED PROPERTY and inserting DISMISSAL IN FAVOR OF FORFEITURE UNDER STATE LAW ;\n**(B)**\nin subsection (a), by striking (a) The Secretary and inserting The Secretary ; and\n**(C)**\nby striking subsections (b) through (d).\n##### (d) Title 31\nSection 9705 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby striking subparagraph (G); and\n**(B)**\nby redesignating subparagraphs (H) through (J) as subparagraphs (G) through (I), respectively; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking paragraphs (2) and (4); and\n**(B)**\nby redesignating paragraphs (3) and (5) as paragraphs (2) and (3), respectively.\n#### 4. Department of justice assets forfeiture fund deposits\nSection 524(c)(4) of title 28, United States Code, is amended\u2014\n**(1)**\nby striking subparagraphs (A) and (B); and\n**(2)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (A) and (B), respectively.\n#### 5. Structuring transactions to evade reporting requirement prohibited\n##### (a) Amendments to title 31\nSection 5324 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting knowingly after Public Law 91\u2013508 ; and\n**(B)**\nin paragraph (3), by inserting of funds not derived from a legitimate source after any transaction ;\n**(2)**\nin subsection (b), in the matter preceding paragraph (1), by inserting knowingly after such section ; and\n**(3)**\nin subsection (c), in the matter preceding paragraph (1), by inserting knowingly after section 5316 .\n##### (b) Probable cause hearing in connection with property seizures relating to certain monetary instruments transactions\n**(1) Amendment**\nSection 5317 of title 31, United States Code, is amended by adding at the end the following:\n(d) Probable cause hearing in connection with property seizures relating to certain monetary instruments transactions (1) In general Not later than 14 days after the date on which notice is provided under paragraph (2)\u2014 (A) a court of competent jurisdiction shall conduct a hearing on any property seized or restrained under subsection (c)(2) with respect to an alleged violation of section 5324; and (B) any property described in subparagraph (A) shall be returned unless the court finds that there is probable cause to believe that there is a violation of section 5324 involving the property. (2) Notice Each person from whom property is seized or restrained under subsection (c)(2) with respect to an alleged violation of section 5324 shall be notified of the right of the person to a hearing under paragraph (1). .\n**(2) Applicability**\nThe amendment made by paragraph (1) shall apply to property seized or restrained after the date of enactment of this Act.\n#### 6. Reporting requirements\nSection 524(c)(6)(A)(i) of title 28, United States Code, is amended by inserting from each type of forfeiture, and specifically identifying which funds were obtained from including criminal forfeitures and which were obtained from civil forfeitures, after deposits .\n#### 7. Applicability\nThe amendments made by this Act shall apply to\u2014\n**(1)**\nany civil forfeiture proceeding pending on or filed on or after the date of enactment of this Act; and\n**(2)**\nany amounts received from the forfeiture of property on or after the date of enactment of this Act.",
      "versionDate": "2025-01-27",
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
        "actionDate": "2026-02-20",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Energy and Commerce, Ways and Means, and Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7638",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FAIR Act of 2026",
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
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-01T15:14:02Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2025-04-01T15:14:02Z"
          },
          {
            "name": "Customs enforcement",
            "updateDate": "2025-04-01T15:14:02Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Evidence and witnesses",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "Property rights",
            "updateDate": "2025-04-01T15:14:01Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-04-01T15:14:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-01T13:20:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-27",
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
          "measure-id": "id119s263",
          "measure-number": "263",
          "measure-type": "s",
          "orig-publish-date": "2025-01-27",
          "originChamber": "SENATE",
          "update-date": "2026-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s263v00",
            "update-date": "2026-01-16"
          },
          "action-date": "2025-01-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fifth Amendment Integrity Restoration Act of 2025 or the FAIR Act of 2025</strong></p><p>This bill establishes more stringent requirements for the federal government with respect to civil asset forfeiture. <em>Civil asset forfeiture</em> generally refers to the seizure and forfeiture of property in connection with federal crimes.</p><p>Specifically, the bill makes various changes to the general rules governing civil forfeiture proceedings. Among the changes, the bill\u00a0</p><ul><li>generally requires the government to notify interested parties within 7 days (currently, 60 days) of a seizure,</li><li>requires an indigent property owner to be represented by counsel regardless of whether the owner requests counsel,</li><li>requires\u00a0the government to meet a higher evidentiary standard in order to prove\u00a0that seized property is connected to a crime, and</li><li>expands the factors\u00a0courts must consider in determining whether a forfeiture of property is constitutionally excessive.</li></ul><p>Additionally, the bill eliminates statutory authority for equitable sharing (i.e., sharing of federally forfeited assets with state, local, or tribal law enforcement agencies that participate in law enforcement efforts resulting in a\u00a0forfeiture). It directs forfeiture proceeds to be deposited into the general fund of the Treasury instead of the Department of Justice (DOJ) Assets Forfeiture Fund.</p><p>The bill requires a prompt probable cause hearing following the seizure of money involved in a structuring offense (i.e., structuring currency transactions to evade currency reporting requirements).</p><p>Finally, the bill requires the annual report on deposits to the DOJ Assets Forfeiture Fund to specify\u00a0total deposits from each type of forfeiture.</p>"
        },
        "title": "FAIR Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s263.xml",
    "summary": {
      "actionDate": "2025-01-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fifth Amendment Integrity Restoration Act of 2025 or the FAIR Act of 2025</strong></p><p>This bill establishes more stringent requirements for the federal government with respect to civil asset forfeiture. <em>Civil asset forfeiture</em> generally refers to the seizure and forfeiture of property in connection with federal crimes.</p><p>Specifically, the bill makes various changes to the general rules governing civil forfeiture proceedings. Among the changes, the bill\u00a0</p><ul><li>generally requires the government to notify interested parties within 7 days (currently, 60 days) of a seizure,</li><li>requires an indigent property owner to be represented by counsel regardless of whether the owner requests counsel,</li><li>requires\u00a0the government to meet a higher evidentiary standard in order to prove\u00a0that seized property is connected to a crime, and</li><li>expands the factors\u00a0courts must consider in determining whether a forfeiture of property is constitutionally excessive.</li></ul><p>Additionally, the bill eliminates statutory authority for equitable sharing (i.e., sharing of federally forfeited assets with state, local, or tribal law enforcement agencies that participate in law enforcement efforts resulting in a\u00a0forfeiture). It directs forfeiture proceeds to be deposited into the general fund of the Treasury instead of the Department of Justice (DOJ) Assets Forfeiture Fund.</p><p>The bill requires a prompt probable cause hearing following the seizure of money involved in a structuring offense (i.e., structuring currency transactions to evade currency reporting requirements).</p><p>Finally, the bill requires the annual report on deposits to the DOJ Assets Forfeiture Fund to specify\u00a0total deposits from each type of forfeiture.</p>",
      "updateDate": "2026-01-16",
      "versionCode": "id119s263"
    },
    "title": "FAIR Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fifth Amendment Integrity Restoration Act of 2025 or the FAIR Act of 2025</strong></p><p>This bill establishes more stringent requirements for the federal government with respect to civil asset forfeiture. <em>Civil asset forfeiture</em> generally refers to the seizure and forfeiture of property in connection with federal crimes.</p><p>Specifically, the bill makes various changes to the general rules governing civil forfeiture proceedings. Among the changes, the bill\u00a0</p><ul><li>generally requires the government to notify interested parties within 7 days (currently, 60 days) of a seizure,</li><li>requires an indigent property owner to be represented by counsel regardless of whether the owner requests counsel,</li><li>requires\u00a0the government to meet a higher evidentiary standard in order to prove\u00a0that seized property is connected to a crime, and</li><li>expands the factors\u00a0courts must consider in determining whether a forfeiture of property is constitutionally excessive.</li></ul><p>Additionally, the bill eliminates statutory authority for equitable sharing (i.e., sharing of federally forfeited assets with state, local, or tribal law enforcement agencies that participate in law enforcement efforts resulting in a\u00a0forfeiture). It directs forfeiture proceeds to be deposited into the general fund of the Treasury instead of the Department of Justice (DOJ) Assets Forfeiture Fund.</p><p>The bill requires a prompt probable cause hearing following the seizure of money involved in a structuring offense (i.e., structuring currency transactions to evade currency reporting requirements).</p><p>Finally, the bill requires the annual report on deposits to the DOJ Assets Forfeiture Fund to specify\u00a0total deposits from each type of forfeiture.</p>",
      "updateDate": "2026-01-16",
      "versionCode": "id119s263"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s263is.xml"
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
      "title": "FAIR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAIR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fifth Amendment Integrity Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restore the integrity of the Fifth Amendment to the Constitution of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:35Z"
    }
  ]
}
```
