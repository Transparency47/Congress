# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/526
- Title: Declaration of Energy Independence Act
- Congress: 119
- Bill type: HR
- Bill number: 526
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-12-17T15:22:45Z
- Update date including text: 2025-12-17T15:22:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/526",
    "number": "526",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Declaration of Energy Independence Act",
    "type": "HR",
    "updateDate": "2025-12-17T15:22:45Z",
    "updateDateIncludingText": "2025-12-17T15:22:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OK"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "UT"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "KS"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr526ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 526\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Ogles (for himself, Mr. Pfluger , Mr. Weber of Texas , Mr. Brecheen , Ms. Hageman , Ms. Maloy , and Mr. Williams of Texas ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Mineral Leasing Act to make certain adjustments to the royalty rates for leases for oil and gas extraction on Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Declaration of Energy Independence Act .\n#### 2. Amendments to Mineral Leasing Act\n##### (a) Onshore oil and gas royalty rates\n**(1) Lease of oil and gas land**\nSection 17 of the Mineral Leasing Act ( 30 U.S.C. 226 ) is amended\u2014\n**(A)**\nby striking 16 2/3 percent each place it appears and inserting 12 1/2 percent ; and\n**(B)**\nin subsection (b)(1)(A), by striking or, in the case of and all that follows through removed or sold from the lease. The and inserting . The .\n**(2) Conditions for reinstatement**\nSection 31(e)(3) of the Mineral Leasing Act ( 30 U.S.C. 188(e)(3) ) is amended by striking 20 each place it appears and inserting 16 2/3 .\n##### (b) Oil and gas minimum bid\nSection 17(b) of the Mineral Leasing Act ( 30 U.S.C. 226(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(B), by striking $10 per acre during the 10-year period beginning on the date of enactment of the Act titled An Act to provide for reconciliation pursuant to title II of S. Con. Res. 14 and inserting $2 per acre for a period of 2 years from the date of enactment of the Federal Onshore Oil and Gas Leasing Reform Act of 1987 ; and\n**(2)**\nin paragraph (2)(C), by striking $10 per acre and inserting $2 per acre .\n##### (c) Fossil fuel rental rates\n**(1) Annual rentals**\nSection 17(d) of the Mineral Leasing Act ( 30 U.S.C. 226(d) ) is amended by striking than $3 per acre per year and all that follows through and $15 per acre per year thereafter and inserting than $1.50 per acre per year for the first through fifth years of the lease and not less than $2 per acre per year for each year thereafter .\n**(2) Rentals in reinstated leases**\nSection 31(e)(2) of the Mineral Leasing Act ( 30 U.S.C. 188(e)(2) ) is amended by striking $20 and inserting $10 .\n##### (d) Elimination of fee for expression of interest\nSection 17 of the Mineral Leasing Act ( 30 U.S.C. 226 ) is amended by striking subsection (q).\n##### (e) Noncompetitive Leasing\nSection 17 of the Mineral Leasing Act ( 30 U.S.C. 226 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)(A)\u2014\n**(i)**\nby striking paragraph (2) and inserting paragraphs (2) and (3) of this subsection ; and\n**(ii)**\nby inserting Lands for which no bids are received or for which the highest bid is less than the national minimum acceptable bid shall be offered promptly within 30 days for leasing under subsection (c) of this section and shall remain available for leasing for a period of 2 years after the competitive lease sale. after the period at the end; and\n**(B)**\nby adding at the end the following:\n(3)(A) If the United States held a vested future interest in a mineral estate that, immediately prior to becoming a vested present interest, was subject to a lease under which oil or gas was being produced, or had a well capable of producing, in paying quantities at an annual average production volume per well per day of either not more than 15 barrels per day of oil or condensate, or not more than 60,000 cubic feet of gas, the holder of the lease may elect to continue the lease as a noncompetitive lease under subsection (c)(1). (B) An election under this paragraph is effective\u2014 (i) in the case of an interest which vested after January 1, 1990, and on or before the date of enactment of this paragraph, if the election is made before the date that is 1 year after the date of enactment of this paragraph; (ii) in the case of an interest which vests within 1 year after the date of enactment of this paragraph, if the election is made before the date that is 2 years after the date of enactment of this paragraph; and (iii) in any case other than those described in clause (i) or (ii), if the election is made prior to the interest becoming a vested present interest. (C) Notwithstanding the consent requirement referenced in section 3 of the Mineral Leasing Act for Acquired Lands ( 30 U.S.C. 352 ), the Secretary shall issue a noncompetitive lease under subsection (c)(1) to a holder who makes an election under subparagraph (A) and who is qualified to hold a lease under this Act. Such lease shall be subject to all terms and conditions under this Act that are applicable to leases issued under subsection (c)(1). (D) A lease issued pursuant to this paragraph shall continue so long as oil or gas continues to be produced in paying quantities. (E) This paragraph shall apply only to those lands under the administration of the Secretary of Agriculture where the United States acquired an interest in such lands pursuant to the Act of March 1, 1911 (36 Stat. 961). ;\n**(2)**\nby striking subsection (c) and inserting the following:\n(c)(1) If the lands to be leased are not leased under subsection (b)(1) of this section or are not subject to competitive leasing under subsection (b)(2) of this section, the person first making application for the lease who is qualified to hold a lease under this Act shall be entitled to a lease of such lands without competitive bidding, upon payment of a non-refundable application fee of at least $75. A lease under this subsection shall be conditioned upon the payment of a royalty at a rate of 12.5 percent in amount or value of the production removed or sold from the lease. Leases shall be issued within 60 days of the date on which the Secretary identifies the first responsible qualified applicant. (2)(A) Lands (i) which were posted for sale under subsection (b)(1) of this section but for which no bids were received or for which the highest bid was less than the national minimum acceptable bid and (ii) for which, at the end of the period referred to in subsection (b)(1) of this section no lease has been issued and no lease application is pending under paragraph (1) of this subsection, shall again be available for leasing only in accordance with subsection (b)(1) of this section. (B) The land in any lease which is issued under paragraph (1) of this subsection or under subsection (b)(1) of this section which lease terminates, expires, is cancelled or is relinquished shall again be available for leasing only in accordance with subsection (b)(1) of this section. ; and\n**(3)**\nby striking subsection (e) and inserting the following:\n(e) Competitive and noncompetitive leases issued under this section shall be for a primary term of 10 years: Provided, however, That competitive leases issued in special tar sand areas shall also be for a primary term of ten years. Each such lease shall continue so long after its primary term as oil or gas is produced in paying quantities. Any lease issued under this section for land on which, or for which under an approved cooperative or unit plan of development or operation, actual drilling operations were commenced prior to the end of its primary term and are being diligently prosecuted at that time shall be extended for two years and so long thereafter as oil or gas is produced in paying quantities. .\n##### (f) Conforming amendments\nSection 31 of the Mineral Leasing Act ( 30 U.S.C. 188 ) is amended\u2014\n**(1)**\nin subsection (d)(1), by inserting or section 17(c) of this Act after pursuant to section 17(b) ;\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby inserting either after rentals and ; and\n**(ii)**\nby inserting or the inclusion in a reinstated lease issued pursuant to the provisions of section 17(c) of this Act of a requirement that future rentals shall be at a rate not less than $5 per acre per year, all after per acre per year, ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nby striking (3) payment and inserting the following:\n(3)(A) payment ; and\n**(ii)**\nby adding at the end the following:\n(B) payment of back royalties and inclusion in a reinstated lease issued pursuant to the provisions of section 17(c) of this Act of a requirement for future royalties at a rate not less than 16\u2154 percent: Provided, That royalty on such reinstated lease shall be paid on all production removed or sold from such lease subsequent to the cancellation or termination of the original lease; and ;\n**(3)**\nby redesignating subsections (f) through (i) as subsections (g) through (j), respectively;\n**(4)**\nby inserting after subsection (e) the following:\n(f) Where an unpatented oil placer mining claim validly located prior to February 24, 1920, which has been or is currently producing or is capable of producing oil or gas, has been or is hereafter deemed conclusively abandoned for failure to file timely the required instruments or copies of instruments required by section 314 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1744 ), and it is shown to the satisfaction of the Secretary that such failure was inadvertent, justifiable, or not due to lack of reasonable diligence on the part of the owner, the Secretary may issue, for the lands covered by the abandoned unpatented oil placer mining claim, a noncompetitive oil and gas lease, consistent with the provisions of section 17(e) of this Act, to be effective from the statutory date the claim was deemed conclusively abandoned. Issuance of such a lease shall be conditioned upon\u2014 (1) a petition for issuance of a noncompetitive oil and gas lease, together with the required rental and royalty, including back rental and royalty accruing from the statutory date of abandonment of the oil placer mining claim, being filed with the Secretary\u2014 (A) with respect to any claim deemed conclusively abandoned on or before the date of enactment of the Federal Oil and Gas Royalty Management Act of 1982, on or before the one hundred and twentieth day after such date of enactment, or (B) with respect to any claim deemed conclusively abandoned after such date of enactment, on or before the one hundred and twentieth day after final notification by the Secretary or a court of competent jurisdiction of the determination of the abandonment of the oil placer mining claim; (2) a valid lease not having been issued affecting any of the lands covered by the abandoned oil placer mining claim prior to the filing of such petition: Provided , however , That after the filing of a petition for issuance of a lease under this subsection, the Secretary shall not issue any new lease affecting any of the lands covered by such abandoned oil placer mining claim for a reasonable period, as determined in accordance with regulations issued by him; (3) a requirement in the lease for payment of rental, including back rentals accruing from the statutory date of abandonment of the oil placer mining claim, of not less than $5 per acre per year; (4) a requirement in the lease for payment of royalty on production removed or sold from the oil placer mining claim, including all royalty on production made subsequent to the statutory date the claim was deemed conclusively abandoned, of not less than 12 1/2 percent; and (5) compliance with the notice and reimbursement of costs provisions of paragraph (4) of subsection (e) but addressed to the petition covering the conversion of an abandoned unpatented oil placer mining claim to a noncompetitive oil and gas lease. ;\n**(5)**\nin subsection (g) (as so redesignated)\u2014\n**(A)**\nin paragraph (1), by striking in the same manner as the original lease issued pursuant to section 17 and inserting as a competitive or a noncompetitive oil and gas lease in the same manner as the original lease issued pursuant to section 17(b) or 17(c) of this Act ;\n**(B)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively;\n**(C)**\nby inserting after paragraph (1) the following:\n(2) Except as otherwise provided in this section, the issuance of a lease in lieu of an abandoned patented oil placer mining claim shall be treated as a noncompetitive oil and gas lease issued pursuant to section 17(c) of this Act. ; and\n**(D)**\nin paragraph (3) (as so redesignated), by inserting applicable to leases issued under subsection 17(c) of this Act ( 30 U.S.C. 226(c) ) after this section, ;\n**(6)**\nin subsection (h) (as so redesignated), by striking subsection (d) and inserting subsections (d) and (f) of this section ; and\n**(7)**\nby striking subsection (i) (as so redesignated) and inserting the following:\n(i)(1) In acting on a petition to issue a noncompetitive oil and gas lease, under subsection (f) of this section or in response to a request filed after issuance of such a lease, or both, the Secretary is authorized to reduce the royalty on such lease if in his judgment it is equitable to do so or the circumstances warrant such relief due to uneconomic or other circumstances which could cause undue hardship or premature termination of production. (2) In acting on a petition for reinstatement pursuant to subsection (d) of this section or in response to a request filed after reinstatement, or both, the Secretary is authorized to reduce the royalty in that reinstated lease on the entire leasehold or any tract or portion thereof segregated for royalty purposes if, in his judgment, there are uneconomic or other circumstances which could cause undue hardship or premature termination of production; or because of any written action of the United States, its agents or employees, which preceded, and was a major consideration in, the lessee's expenditure of funds to develop the property under the lease after the rent had become due and had not been paid; or if in the judgment of the Secretary it is equitable to do so for any reason. .",
      "versionDate": "2025-01-16",
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
        "name": "Energy",
        "updateDate": "2025-02-13T19:50:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr526",
          "measure-number": "526",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-12-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr526v00",
            "update-date": "2025-12-17"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Declaration of Energy Independence Act</strong></p><p>This bill reduces certain royalty rates, minimum bids, rental rates, and fees for onshore oil and gas leases on federal lands\u00a0and modifies related leasing procedures.</p><p>Specifically, the bill (1) decreases the royalty rate from 16 2/3% to 12 1/2% for\u00a0developing oil and gas on federal lands, (2) lowers the minimum bid amount from $10.00 to $2.00 per acre for oil and gas leases on federal lands, and (3) decreases the rental rates from a maximum of $15.00 per acre to $1.50 per acre for the first five years and $2.00 per acre thereafter.\u00a0The bill\u00a0also eliminates the fee for expressing interest in a lease.\u00a0</p><p>It also modifies\u00a0leasing procedures to provide for noncompetitive leasing\u00a0under certain circumstances.</p><p>In addition, the bill modifies the conditions\u00a0for the reinstatement of leases that have been cancelled or terminated, including by reducing the applicable royalty and rental rates.</p>"
        },
        "title": "Declaration of Energy Independence Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr526.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Declaration of Energy Independence Act</strong></p><p>This bill reduces certain royalty rates, minimum bids, rental rates, and fees for onshore oil and gas leases on federal lands\u00a0and modifies related leasing procedures.</p><p>Specifically, the bill (1) decreases the royalty rate from 16 2/3% to 12 1/2% for\u00a0developing oil and gas on federal lands, (2) lowers the minimum bid amount from $10.00 to $2.00 per acre for oil and gas leases on federal lands, and (3) decreases the rental rates from a maximum of $15.00 per acre to $1.50 per acre for the first five years and $2.00 per acre thereafter.\u00a0The bill\u00a0also eliminates the fee for expressing interest in a lease.\u00a0</p><p>It also modifies\u00a0leasing procedures to provide for noncompetitive leasing\u00a0under certain circumstances.</p><p>In addition, the bill modifies the conditions\u00a0for the reinstatement of leases that have been cancelled or terminated, including by reducing the applicable royalty and rental rates.</p>",
      "updateDate": "2025-12-17",
      "versionCode": "id119hr526"
    },
    "title": "Declaration of Energy Independence Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Declaration of Energy Independence Act</strong></p><p>This bill reduces certain royalty rates, minimum bids, rental rates, and fees for onshore oil and gas leases on federal lands\u00a0and modifies related leasing procedures.</p><p>Specifically, the bill (1) decreases the royalty rate from 16 2/3% to 12 1/2% for\u00a0developing oil and gas on federal lands, (2) lowers the minimum bid amount from $10.00 to $2.00 per acre for oil and gas leases on federal lands, and (3) decreases the rental rates from a maximum of $15.00 per acre to $1.50 per acre for the first five years and $2.00 per acre thereafter.\u00a0The bill\u00a0also eliminates the fee for expressing interest in a lease.\u00a0</p><p>It also modifies\u00a0leasing procedures to provide for noncompetitive leasing\u00a0under certain circumstances.</p><p>In addition, the bill modifies the conditions\u00a0for the reinstatement of leases that have been cancelled or terminated, including by reducing the applicable royalty and rental rates.</p>",
      "updateDate": "2025-12-17",
      "versionCode": "id119hr526"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr526ih.xml"
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
      "title": "Declaration of Energy Independence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T12:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Declaration of Energy Independence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Mineral Leasing Act to make certain adjustments to the royalty rates for leases for oil and gas extraction on Federal land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T12:03:27Z"
    }
  ]
}
```
