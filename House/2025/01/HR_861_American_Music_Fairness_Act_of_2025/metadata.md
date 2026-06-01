# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/861?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/861
- Title: American Music Fairness Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 861
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2026-02-24T09:05:47Z
- Update date including text: 2026-02-24T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/861",
    "number": "861",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "American Music Fairness Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:47Z",
    "updateDateIncludingText": "2026-02-24T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:03:50Z",
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
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TN"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MD"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "WA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "PA"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr861ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 861\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Issa (for himself, Mr. Nadler , Mr. Green of Tennessee , Mr. McClintock , and Mr. Lieu ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 17, United States Code, to provide fair treatment of radio stations and artists for the use of sound recordings, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the American Music Fairness Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Equitable treatment for terrestrial broadcasts and internet services.\nSec. 3. Timing of proceedings under sections 112(e) and 114(f).\nSec. 4. Special protection for small broadcasters.\nSec. 5. Distribution of certain royalties.\nSec. 6. No harmful effects on songwriters.\nSec. 7. Value of promotion taken into account.\n#### 2. Equitable treatment for terrestrial broadcasts and internet services\n##### (a) Performance right applicable to audio transmissions generally\nParagraph (6) of section 106 of title 17, United States Code, is amended to read as follows:\n(6) in the case of sound recordings, to perform the copyrighted work publicly by means of an audio transmission. .\n##### (b) Inclusion of terrestrial broadcasts in existing performance right and statutory license\nSection 114(d)(1) of title 17, United States Code, is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking a digital and inserting an ;\n**(2)**\nby striking subparagraph (A);\n**(3)**\nby redesignating subparagraphs (B) and (C) as (A) and (B), respectively; and\n**(4)**\nin subparagraph (A), as redesignated by paragraph (3), by striking nonsubscription each place such term appears and inserting licensed nonsubscription .\n##### (c) Technical and conforming amendments\n**(1) Definition**\nSection 101 of title 17, United States Code, is amended by inserting after the definition of architectural work the following:\nAn audio transmission is a transmission of a sound recording, whether in a digital, analog, or other format. This term does not include the transmission of any audiovisual work. .\n**(2) Conforming removal of digital**\nTitle 17, United States Code, is amended\u2014\n**(A)**\nin section 112(e)(8), by striking a digital audio transmission and inserting an audio transmission ;\n**(B)**\nin section 114\u2014\n**(i)**\nin subsection (d)\u2014\n**(I)**\nin paragraph (2)\u2014\n**(aa)**\nin the matter preceding subparagraph (A), by striking subscription digital and inserting subscription ; and\n**(bb)**\nin subparagraph (C)(viii), by striking digital signal and inserting signal ; and\n**(II)**\nin paragraph (4)\u2014\n**(aa)**\nin subparagraph (A), by striking a digital audio transmission and inserting an audio transmission ; and\n**(bb)**\nin subparagraph (B)(i), by striking a digital audio transmission and inserting an audio transmission ;\n**(ii)**\nin subsection (g)(2)(A), by striking a digital and inserting an ; and\n**(iii)**\nin subsection (j)\u2014\n**(I)**\nin paragraph (6)\u2014\n**(aa)**\nby striking digital ; and\n**(bb)**\nby striking retransmissions of broadcast transmissions and inserting broadcast transmissions and retransmissions of broadcast transmissions ; and\n**(II)**\nin paragraph (8), by striking subscription digital and inserting subscription ; and\n**(C)**\nin section 1401\u2014\n**(i)**\nin subsection (b), by striking a digital audio and inserting an audio ; and\n**(ii)**\nin subsection (d)\u2014\n**(I)**\nin paragraph (1), by striking a digital audio and inserting an audio ;\n**(II)**\nin paragraph (2)(A), by striking a digital audio and inserting an audio ; and\n**(III)**\nin paragraph (4)(A), by striking a digital audio and inserting an audio .\n#### 3. Timing of proceedings under sections 112( e ) and 114( f )\nParagraph (3) of section 804(b) of title 17, United States Code, is amended by adding at the end the following new subparagraph:\n(D) A proceeding under this chapter shall be commenced as soon as practicable after the date of the enactment of this subparagraph to determine royalty rates and terms for nonsubscription broadcast transmissions, to be effective for the period beginning on such date of enactment, and ending on December 31, 2028. Any payment due under section 114(f)(1)(D) shall not be due until the due date of the first royalty payments for nonsubscription broadcast transmissions that are determined, after the date of the enactment of this subparagraph, by the Copyright Royalty Judges. Thereafter, such proceeding shall be repeated in each subsequent fifth calendar year. .\n#### 4. Special protection for small broadcasters\n##### (a) Specified royalty fees\nSection 114(f)(1) of title 17, United States Code, is amended by inserting at the end the following new subparagraph:\n(D) (i) Notwithstanding the provisions of subparagraphs (A) through (C), the royalty rate shall be as follows for nonsubscription broadcast transmissions by each individual terrestrial broadcast station licensed as such by the Federal Communications Commission that satisfies the conditions in clause (ii)\u2014 (I) $10 per calendar year, in the case of nonsubscription broadcast transmissions by a broadcast station that generated revenue in the immediately preceding calendar year of less than $100,000; (II) $100 per calendar year, in the case of nonsubscription broadcast transmissions by a broadcast station that is a public broadcasting entity as defined in section 118(f) and generated revenue in the immediately preceding calendar year of $100,000 or more, but less than $1,500,000; and (III) $500 per calendar year, in the case of nonsubscription broadcast transmissions by a broadcast station that is not a public broadcasting entity as defined in section 118(f) and generated revenue in the immediately preceding calendar year of $100,000 or more, but less than $1,500,000. (ii) An individual terrestrial broadcast station licensed as such by the Federal Communications Commission is eligible for a royalty rate set forth in clause (i) if\u2014 (I) the revenue from the operation of that individual station was less than $1,500,000 during the immediately preceding calendar year; (II) the aggregate revenue of the owner and operator of the broadcast station and any person directly or indirectly controlling, controlled by, or under common control with such owner or operator, from any source, was less than $10,000,000 during the immediately preceding calendar year; and (III) the owner or operator of the broadcast station provides to the nonprofit collective designated by the Copyright Royalty Judges to distribute receipts from the licensing of transmissions in accordance with subsection (f), by no later than January 31 of the relevant calendar year, a written and signed certification of the station\u2019s eligibility under this clause and the applicable subclause of clause (i), in accordance with requirements the Copyright Royalty Judges shall prescribe by regulation. (iii) For purposes of clauses (i) and (ii)\u2014 (I) revenue shall be calculated in accordance with generally accepted accounting principles; (II) revenue generated by a terrestrial broadcast station shall include all revenue from the operation of the station, from any source; and (III) in the case of affiliated broadcast stations, revenue shall be allocated reasonably to individual stations associated with the revenue. (iv) The royalty rates specified in clause (i) shall not be admissible as evidence or otherwise taken into account in determining royalty rates in a proceeding under chapter 8, or in any other administrative, judicial, or other Federal Government proceeding involving the setting or adjustment of the royalties payable for the public performance or reproduction in ephemeral phonorecords or copies of sound recordings, the determination of terms or conditions related thereto, or the establishment of notice or recordkeeping requirements. .\n##### (b) Technical correction\nSection 118(f) of title 17, United States Code, is amended by striking section 397 of title 47 and inserting section 397 of the Communications Act of 1934 ( 47 U.S.C. 397 ) .\n#### 5. Distribution of certain royalties\nSection 114(g) of title 17, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting or in the case of a transmission to which paragraph (5) applies after this section ;\n**(2)**\nby redesignating paragraphs (5), (6), and (7) as (6), (7), and (8), respectively; and\n**(3)**\nby inserting after paragraph (4) the following new paragraph:\n(5) Notwithstanding paragraph (1), to the extent that a license granted by the copyright owner of a sound recording to a transmitting entity eligible for a statutory license under subsection (d)(2) extends to such entity\u2019s transmissions otherwise licensable under a statutory license in accordance with subsection (f), such entity shall pay to the collective designated to distribute statutory licensing receipts from the licensing of transmissions in accordance with subsection (f), 50 percent of the total royalties that such entity is required, pursuant to the applicable license agreement, to pay for such transmissions otherwise licensable under a statutory license in accordance with subsection (f). That collective shall distribute such payments in proportion to the distributions provided in subparagraphs (B) through (D) of paragraph (2), and such payments shall be the only payments to which featured and nonfeatured artists are entitled by virtue of such transmissions under the direct license with such entity. .\n#### 6. No harmful effects on songwriters\nNothing in this Act, or the amendments made by this Act, shall adversely affect in any respect the public performance rights of or royalties payable to songwriters or copyright owners of musical works.\n#### 7. Value of promotion taken into account\nPursuant to section 114(f)(1)(B) of title 17, United States Code, in determining rates and terms for terrestrial broadcast radio stations under this Act, and the amendments made by this Act, the Copyright Royalty Judges shall base their decision on economic, competitive, and programming information presented by the parties, including whether use of the station\u2019s service may substitute for or may promote the sales of phonorecords or otherwise may interfere with or may enhance the sound recording copyright owner\u2019s other streams of revenue from the copyright owner\u2019s sound recordings.",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "326",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Music Fairness Act",
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
        "name": "Commerce",
        "updateDate": "2025-03-04T14:40:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr861",
          "measure-number": "861",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr861v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Music Fairness Act of\u00a02025</strong></p><p>This bill establishes that the copyright holder of a sound recording shall have the exclusive right to perform the sound recording through an audio transmission. (Currently, the public performance right only covers performances through a digital audio transmission in certain instances, which means that nonsubscription terrestrial radio stations generally do not have to get a license to publicly perform a copyright-protected sound recording.)</p><p>Under the bill, a nonsubscription broadcast transmission must have a license to publicly perform such sound recordings. The Copyright Royalty Board must periodically determine the royalty rates for such a license. When determining the rates, the board must base its decision on certain information presented by the parties, including the radio stations' effect on other streams of revenue related to the sound recordings.</p><p>Terrestrial broadcast stations (and the owners of such stations) that fall below certain revenue thresholds may pay certain flat fees, instead of the board-established rate, for a license to publicly perform copyright-protected sound recordings.</p>"
        },
        "title": "American Music Fairness Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr861.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Music Fairness Act of\u00a02025</strong></p><p>This bill establishes that the copyright holder of a sound recording shall have the exclusive right to perform the sound recording through an audio transmission. (Currently, the public performance right only covers performances through a digital audio transmission in certain instances, which means that nonsubscription terrestrial radio stations generally do not have to get a license to publicly perform a copyright-protected sound recording.)</p><p>Under the bill, a nonsubscription broadcast transmission must have a license to publicly perform such sound recordings. The Copyright Royalty Board must periodically determine the royalty rates for such a license. When determining the rates, the board must base its decision on certain information presented by the parties, including the radio stations' effect on other streams of revenue related to the sound recordings.</p><p>Terrestrial broadcast stations (and the owners of such stations) that fall below certain revenue thresholds may pay certain flat fees, instead of the board-established rate, for a license to publicly perform copyright-protected sound recordings.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr861"
    },
    "title": "American Music Fairness Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Music Fairness Act of\u00a02025</strong></p><p>This bill establishes that the copyright holder of a sound recording shall have the exclusive right to perform the sound recording through an audio transmission. (Currently, the public performance right only covers performances through a digital audio transmission in certain instances, which means that nonsubscription terrestrial radio stations generally do not have to get a license to publicly perform a copyright-protected sound recording.)</p><p>Under the bill, a nonsubscription broadcast transmission must have a license to publicly perform such sound recordings. The Copyright Royalty Board must periodically determine the royalty rates for such a license. When determining the rates, the board must base its decision on certain information presented by the parties, including the radio stations' effect on other streams of revenue related to the sound recordings.</p><p>Terrestrial broadcast stations (and the owners of such stations) that fall below certain revenue thresholds may pay certain flat fees, instead of the board-established rate, for a license to publicly perform copyright-protected sound recordings.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr861"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr861ih.xml"
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
      "title": "American Music Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Music Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 17, United States Code, to provide fair treatment of radio stations and artists for the use of sound recordings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T09:03:27Z"
    }
  ]
}
```
