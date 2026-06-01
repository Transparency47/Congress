# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2724
- Title: Safe at Home Act
- Congress: 119
- Bill type: S
- Bill number: 2724
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2025-09-23T15:26:08Z
- Update date including text: 2025-09-23T15:26:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2724",
    "number": "2724",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Safe at Home Act",
    "type": "S",
    "updateDate": "2025-09-23T15:26:08Z",
    "updateDateIncludingText": "2025-09-23T15:26:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T18:06:25Z",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2724is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2724\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Ms. Klobuchar (for herself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require executive agencies and Federal courts to comply with address confidentiality programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe at Home Act .\n#### 2. Executive agency and Federal court compliance with State address confidentiality programs\n##### (a) Definitions\nIn this section:\n**(1) Address confidentiality program**\nThe term address confidentiality program means a program implemented pursuant to State law that\u2014\n**(A)**\nprovides a designated address;\n**(B)**\nprovides a mail-forwarding service; and\n**(C)**\nis designated by a participant as the legal agent of the participant to receive service of process.\n**(2) Designated address**\nThe term designated address means an address assigned by an address confidentiality program for a participant to use in lieu of the physical address of the participant.\n**(3) Executive agency**\n**(A) In general**\nThe term executive agency has the meaning given the term Executive agency in section 105 of title 5, United States Code.\n**(B) Exception**\nThe term executive agency does not include the Census Bureau.\n**(4) Participant**\nThe term participant means an adult or minor who is enrolled in an address confidentiality program.\n**(5) Physical address**\nThe term physical address means the actual home, school, or employment address of a participant.\n**(6) State**\nThe term State means each of the States, the District of Columbia, each territory or possession of the United States, and each federally recognized Indian Tribe.\n##### (b) Acceptance of address confidentiality program\nEach executive agency and Federal court shall accept, for any purpose for which an individual is required to provide an address to the agency or court, an address designated to that individual pursuant to an address confidentiality program.\n##### (c) Exemption from liability\nA participant shall not be subject to Federal regulatory, civil, or criminal penalties for providing a designated address in lieu of the physical address of the participant to an executive agency or Federal court.\n##### (d) Regulatory compliance with address confidentiality programs\nNot later than 1 year after the date of enactment of this Act, each executive agency shall review and, as necessary, modify existing regulations to comply with this Act.\n##### (e) Compliance with address confidentiality program procedures and exemption from FOIA\n**(1) In general**\nSubject to paragraphs (3) and (4), in the case of an executive agency or Federal court seeking to acquire the physical address of a participant, the agency or court shall comply with any applicable procedures of the applicable address confidentiality program for acquiring such address.\n**(2) FOIA exemption**\nUpon acquiring a physical address under paragraph (1), the physical address\u2014\n**(A)**\nshall be considered confidential; and\n**(B)**\nshall be exempt from disclosure under section 552 of title 5, United States Code (commonly referred to as the Freedom of Information Act ) for the purpose of subsection (b)(3) of that section.\n**(3) Law enforcement exception**\n**(A) In general**\nWhen the physical address of a participant is relevant to a Federal criminal proceeding, a Federal court may order the disclosure of the physical address to relevant parties without regard to the procedures of the relevant address confidentiality program, including\u2014\n**(i)**\ncourt officers and employees;\n**(ii)**\nsupervision and probation officers;\n**(iii)**\nprosecutors;\n**(iv)**\nlaw enforcement officers; and\n**(v)**\nany other party determined relevant by the Federal court.\n**(B) Limitations**\nIf a Federal court orders the disclosure of a physical address to a party under subparagraph (A), the party\u2014\n**(i)**\nshall keep the physical address confidential; and\n**(ii)**\nmay only use the physical address for the purpose for which the Federal court orders the disclosure.\n**(4) Administration exception**\nIf an executive agency requires the physical address of a participant in order for the executive agency to carry out the requirements of Federal law, a Federal court may order the disclosure of the physical address to the executive agency if the head of the executive agency makes a written request to the relevant address confidentiality program that maintains the record specifying\u2014\n**(A)**\nthe particular portion of the record desired; and\n**(B)**\nthe activity for which the record is sought.\n**(5) Rule of construction**\nNothing in this subsection shall be construed to require an executive agency to be subject to an audit performed by a State.\n##### (f) Prompt notification upon termination from participation\nIf the participation of an individual in an address confidentiality program is terminated, that individual shall promptly notify each executive agency or Federal court that accepted a designated address under subsection (b).",
      "versionDate": "2025-09-04",
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
        "name": "Law",
        "updateDate": "2025-09-23T15:26:08Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2724is.xml"
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
      "title": "Safe at Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe at Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-16T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require executive agencies and Federal courts to comply with address confidentiality programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-16T04:48:21Z"
    }
  ]
}
```
