# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1420
- Title: Child Care Nutrition Enhancement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1420
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-17T14:32:46Z
- Update date including text: 2026-03-17T14:32:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1420",
    "number": "1420",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Child Care Nutrition Enhancement Act of 2025",
    "type": "S",
    "updateDate": "2026-03-17T14:32:46Z",
    "updateDateIncludingText": "2026-03-17T14:32:46Z"
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
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
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
          "date": "2025-04-10T17:09:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NH"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-04-10",
      "state": "VT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "RI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1420is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1420\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Blumenthal (for himself, Ms. Smith , Mrs. Shaheen , Ms. Warren , Mr. Welch , Ms. Hirono , Mr. Sanders , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Richard B. Russell National School Lunch Act to increase the amount of reimbursements under the child and adult care food program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Child Care Nutrition Enhancement Act of 2025 .\n#### 2. Reimbursements under child and adult care food program\n##### (a) In general\nSection 17 of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nin each of paragraphs (1), (2), and (3), by inserting and subject to paragraph (7) after subsection (f)(3) each place it appears; and\n**(B)**\nby adding at the end the following:\n(7) Additional reimbursement Beginning on the first day of the first month that begins after the date of enactment of the Child Care Nutrition Enhancement Act of 2025 , each meal and supplement served under this section shall receive an additional reimbursement in the amount of 10 cents (as adjusted pursuant to section 11(a)). ;\n**(2)**\nin subsection (o)(3)(A), in the first sentence, by striking consulation and inserting consultation ; and\n**(3)**\nin subsection (r)(4)(B)(ii), by striking subsection (c)(3) and inserting paragraphs (3) and (7) of subsection (c) .\n##### (b) Reimbursement of family or group day care home sponsoring organizations\nSection 17(f)(3) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1766(f)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (ii)\u2014\n**(i)**\nin the heading, by striking Tier i family or group day care homes and inserting Calculation of reimbursement ;\n**(ii)**\nby striking subclause (I);\n**(iii)**\nby redesignating subclauses (II), (III), and (IV) as subclauses (I), (II), and (III), respectively;\n**(iv)**\nin subclause (I) (as so redesignated)\u2014\n**(I)**\nby striking subclause (III), a tier I and inserting subclause (II), a ; and\n**(II)**\nby striking , except that and all that follows through section 9 ;\n**(v)**\nin subclause (II) (as so redesignated)\u2014\n**(I)**\nby striking subclause (IV) and inserting subclause (III) ; and\n**(II)**\nby striking subclause (II) and inserting subclause (I) ; and\n**(vi)**\nby adding at the end the following:\n(IV) Additional reimbursement The additional reimbursement amount required under subsection (c)(7) shall apply to the reimbursements of meals and supplements under this subparagraph. ; and\n**(B)**\nby striking clause (iii); and\n**(2)**\nby striking subparagraph (E).",
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
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2859",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Child Care Nutrition Enhancement Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T13:39:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1420",
          "measure-number": "1420",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1420v00",
            "update-date": "2026-03-17"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Child Care Nutrition Enhancement Act of 2025</strong></p><p>This bill increases and modifies reimbursements for meals and snacks served under the Child and Adult Care Food Program (CACFP).</p><p>CACFP is a Food and Nutrition Service program that provides federal reimbursements for meals and snacks provided to eligible children and adults who are enrolled at participating child care centers, day care homes (i.e., private homes that provide nonresidential child care services), and adult day care centers.</p><p>Specifically, the bill eliminates the two-tiered system for\u00a0CACFP reimbursement rates for day care homes and generally makes all day care homes eligible for the same reimbursement rates.\u00a0Under current law, day care homes located in a low-income area or with a low-income provider receive higher reimbursement rates (i.e., Tier I rates). Day care homes that do not qualify for Tier I rates receive Tier II rates, which are lower.</p><p>Further, the bill provides an additional 10-cent reimbursement for each eligible meal and snack served in the CACFP.</p><p>The bill also allows the provider of a family or group day care home to serve reimbursable meals and snacks to their own children\u00a0when serving meals and snacks to children in their care. Specifically, the bill eliminates the current requirement that the child of a day care home provider meet the program's income eligibility requirement in order for the day care provider to receive reimbursement for the meals and snacks served to their child.</p>"
        },
        "title": "Child Care Nutrition Enhancement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1420.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Child Care Nutrition Enhancement Act of 2025</strong></p><p>This bill increases and modifies reimbursements for meals and snacks served under the Child and Adult Care Food Program (CACFP).</p><p>CACFP is a Food and Nutrition Service program that provides federal reimbursements for meals and snacks provided to eligible children and adults who are enrolled at participating child care centers, day care homes (i.e., private homes that provide nonresidential child care services), and adult day care centers.</p><p>Specifically, the bill eliminates the two-tiered system for\u00a0CACFP reimbursement rates for day care homes and generally makes all day care homes eligible for the same reimbursement rates.\u00a0Under current law, day care homes located in a low-income area or with a low-income provider receive higher reimbursement rates (i.e., Tier I rates). Day care homes that do not qualify for Tier I rates receive Tier II rates, which are lower.</p><p>Further, the bill provides an additional 10-cent reimbursement for each eligible meal and snack served in the CACFP.</p><p>The bill also allows the provider of a family or group day care home to serve reimbursable meals and snacks to their own children\u00a0when serving meals and snacks to children in their care. Specifically, the bill eliminates the current requirement that the child of a day care home provider meet the program's income eligibility requirement in order for the day care provider to receive reimbursement for the meals and snacks served to their child.</p>",
      "updateDate": "2026-03-17",
      "versionCode": "id119s1420"
    },
    "title": "Child Care Nutrition Enhancement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Child Care Nutrition Enhancement Act of 2025</strong></p><p>This bill increases and modifies reimbursements for meals and snacks served under the Child and Adult Care Food Program (CACFP).</p><p>CACFP is a Food and Nutrition Service program that provides federal reimbursements for meals and snacks provided to eligible children and adults who are enrolled at participating child care centers, day care homes (i.e., private homes that provide nonresidential child care services), and adult day care centers.</p><p>Specifically, the bill eliminates the two-tiered system for\u00a0CACFP reimbursement rates for day care homes and generally makes all day care homes eligible for the same reimbursement rates.\u00a0Under current law, day care homes located in a low-income area or with a low-income provider receive higher reimbursement rates (i.e., Tier I rates). Day care homes that do not qualify for Tier I rates receive Tier II rates, which are lower.</p><p>Further, the bill provides an additional 10-cent reimbursement for each eligible meal and snack served in the CACFP.</p><p>The bill also allows the provider of a family or group day care home to serve reimbursable meals and snacks to their own children\u00a0when serving meals and snacks to children in their care. Specifically, the bill eliminates the current requirement that the child of a day care home provider meet the program's income eligibility requirement in order for the day care provider to receive reimbursement for the meals and snacks served to their child.</p>",
      "updateDate": "2026-03-17",
      "versionCode": "id119s1420"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1420is.xml"
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
      "title": "Child Care Nutrition Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Child Care Nutrition Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T02:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Richard B. Russell National School Lunch Act to increase the amount of reimbursements under the child and adult care food program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:19Z"
    }
  ]
}
```
