# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8059?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8059
- Title: Unserialized Firearm Harm Oversight and Serialization Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8059
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-04-10T12:54:19Z
- Update date including text: 2026-04-10T12:54:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8059",
    "number": "8059",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Unserialized Firearm Harm Oversight and Serialization Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-10T12:54:19Z",
    "updateDateIncludingText": "2026-04-10T12:54:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-24T16:00:20Z",
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
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MO"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "OR"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NJ"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8059ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8059\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mr. Min (for himself, Mr. Bell , Mrs. Hayes , Ms. Salinas , Ms. Garcia of Texas , Mr. Gottheimer , Mr. Goldman of New York , Mrs. Grijalva , and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require serialization of firearms produced through additive manufacturing and of unserialized firearms possessed by federally licensed firearms dealers and gunsmiths, to establish penalties for violations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unserialized Firearm Harm Oversight and Serialization Act of 2026 .\n#### 2. Codification of Supreme Court decision clarifying that certain firearm assembly kits are firearms\nSection 921(a)(3)(A) of title 18, United States Code, is amended by inserting , and any combination of parts which is clearly intended to function, or may readily be converted, before to expel a projectile .\n#### 3. Serialization requirement for firearms produced through additive manufacturing\n##### (a) In general\nSection 923(i) of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting (1) after (i) ; and\n**(2)**\nby adding after and below the end the following:\n(2) A person licensed under this section who produces or completes a frame or receiver for a firearm, or a collection of parts that, with other readily available parts, could be used to produce a firearm, through additive manufacturing or any other process involving the use of a technology, machine, or device that enables the creation of such components other than by traditional manufacturing methods, for sale or transfer in or affecting interstate or foreign commerce, shall cast or engrave a serial number on the receiver or frame or each part in the collection. .\n##### (b) Definitions\nSection 921(a) of such title is amended by adding at the end the following:\n(39) The term additive manufacturing means a process of joining materials to make objects from 3-dimensional model data, usually layer upon layer, including powder bed fusion, material extrusion, directed energy deposition, vat photopolymerization, and binder jetting. (40) The term non-traditional manufacturing method means any process of producing a firearm, frame, or receiver outside of conventional manufacturing, including additive manufacturing, digital fabrication, or other emerging technologies. .\n##### (c) Penalties\nSection 924 of such title is amended by adding at the end the following:\n(q) Penalties relating to requirement that firearms produced through additive manufacturing have serial numbers (1) Civil penalty for 1 st offense Whoever knowingly violates section 923(i)(2) shall be subject to a civil penalty of not more than $10,000. (2) Criminal penalties for subsequent offense Whoever, having been convicted of violating section 923(i)(2), willfully violates such section shall be fined not more than $100,000, imprisoned not less than 1 year, or both. .\n#### 4. Requirement that licensed dealer serialize unserialized firearms taken into inventory\n##### (a) In general\nSection 923(i) of title 18, United States Code, as amended by section 3(a) of this Act, is amended by adding at the end the following:\n(3) A person licensed under this section who receives a firearm that does not have a serial number engraved or cast on the receiver or frame of the firearm shall\u2014 (A) engrave or cast a serial number on the receiver or frame of the firearm, in such manner as the Attorney General shall by regulations prescribe; (B) transmit to the Attorney General a record of the receipt, which shall set forth the serial number; and (C) keep and maintain a copy of the record. .\n##### (b) Use of serial number information only in active criminal investigations\nSection 923(i) of such title, as amended by section 3(a) of this Act and subsection (a) of this section, is amended by adding at the end the following:\n(4) The Attorney General may use information in a record transmitted under paragraph (3)(B) of this subsection only in the course of an ongoing bona fide criminal investigation. The 2nd sentence of section 926(a) shall not apply with respect to the information in any such record. .\n#### 5. Firearm dealer serialization credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Firearm dealer serialization credit (a) In general For purposes of section 38, in the case of a taxpayer who is licensed under section 923 of title 18, United States Code, to engage in the business of importing, manufacturing, or dealing in firearms, the firearm dealer serialization credit determined under this section for the taxable year shall be an amount equal to the firearm serialization expenditures of the taxpayer for the taxable year. (b) Firearm serialization expenditures For purposes of this section, the term firearm serialization expenditures means any amounts paid or incurred during the taxable year to comply with section 923(i)(3) of title 18, United States Code, including the purchase or lease of equipment (or related software) for the engraving or casting of firearms. (c) Limitation The amount of firearm serialization expenditures taken into account by the taxpayer under subsection (a) for any taxable year shall not exceed\u2014 (1) in the case of amounts paid or incurred for the purchase or lease of equipment (or related software) for engraving or casting firearm receivers or frames, $1,000, and (2) in the case of any other expenditures, the lesser of\u2014 (A) an amount that does not exceed $50 for each firearm the engraving or casting of which is required of the taxpayer under section 923(i)(3) of title 18, United States Code, or (B) $1,500. (d) Controlled groups Rules similar to the rules of paragraphs (1) and (2) of section 41(f) shall apply for purposes of this section. (e) Denial of double benefit (1) No deduction No deduction shall be allowed for any expenditures taken into account in determining the credit under this section for the taxable year. (2) Basis adjustment If a credit is determined under this section with respect to any property purchased by the taxpayer, the basis of such property shall be reduced by the amount of the credit so determined with respect to such property. (f) Termination (1) In general Except to the extent provided in paragraph (2), this section shall not apply to any amount paid or incurred more than 5 years after the date of the enactment of this section. (2) Extension If the Secretary (after consultation with the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives) certifies to Congress that the credit allowed under this section has improved firearm serialization and compliance with related Federal law, paragraph (1) shall be applied by substituting 7 years for 5 years . .\n##### (b) Credit made part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the firearm dealer serialization credit determined under section 45BB(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Firearm dealer serialization credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act.\n#### 6. Relationship to State law\nNo amendment made by this Act shall be interpreted to supersede State law.\n#### 7. Effective date\nExcept as provided in section 5(d), the amendments made by this Act shall take effect 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-03-24",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-10T12:54:19Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8059ih.xml"
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
      "title": "Unserialized Firearm Harm Oversight and Serialization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Unserialized Firearm Harm Oversight and Serialization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require serialization of firearms produced through additive manufacturing and of unserialized firearms possessed by federally licensed firearms dealers and gunsmiths, to establish penalties for violations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:29Z"
    }
  ]
}
```
