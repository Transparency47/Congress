# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7363?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7363
- Title: ICE Out of Our Faces Act
- Congress: 119
- Bill type: HR
- Bill number: 7363
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-05-16T08:07:07Z
- Update date including text: 2026-05-16T08:07:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-05 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-04 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-05 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7363",
    "number": "7363",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "J000298",
        "district": "7",
        "firstName": "Pramila",
        "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
        "lastName": "Jayapal",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "ICE Out of Our Faces Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:07Z",
    "updateDateIncludingText": "2026-05-16T08:07:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-05T05:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-04T15:03:05Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "OR"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "MD"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "DC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "TN"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7363ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7363\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Jayapal introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the Department of Homeland Security\u2019s use of facial recognition.\n#### 1. Short title\nThis Act may be cited as the ICE Out of Our Faces Act .\n#### 2. Definitions\nIn this Act:\n**(1) Biometric surveillance system**\nThe term biometric surveillance system means computer software that performs facial recognition or other biometric recognition in real time or on a recording or photograph.\n**(2) Covered immigration officer**\nThe term covered immigration officer means any individual who is\u2014\n**(A)**\nauthorized to perform immigration enforcement functions; and\n**(B)**\n**(i)**\nan officer, employee, agent, contractor, or subcontractor of U.S. Customs and Border Protection;\n**(ii)**\nan officer, employee, agent, contractor, or subcontractor of U.S. Immigration and Customs Enforcement; or\n**(iii)**\nan individual authorized, deputized, or designated to perform immigration enforcement functions pursuant to section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ).\n**(3) Facial recognition**\nThe term facial recognition means an automated or semi-automated process that\u2014\n**(A)**\nassists in identifying an individual, capturing information about an individual, matching an individual to a list or otherwise generating or assisting in generating surveillance or identification information about an individual based on the physical characteristics of the individual\u2019s face; or\n**(B)**\nlogs characteristics of an individual\u2019s face, head, or body to infer emotion, associations, activities, or the location of an individual.\n**(4) Other biometric recognition**\nThe term other biometric recognition \u2014\n**(A)**\nmeans an automated or semi-automated process that\u2014\n**(i)**\nassists in identifying an individual, capturing information about an individual, or otherwise generating or assisting in generating surveillance information about an individual based on the characteristics of the individual\u2019s gait or other immutable characteristic ascertained from a distance;\n**(ii)**\nuses voice recognition technology; or\n**(iii)**\nlogs characteristics referred to in clause (i) or (ii) to infer emotion, associations, activities, or the location of an individual; and\n**(B)**\ndoes not include identification based on fingerprints or palm prints not ascertained from a distance.\n**(5) Voice recognition technology**\nThe term voice recognition technology means an automated or semi-automated process that assists in identifying or verifying an individual based on the characteristics of an individual\u2019s voice.\n#### 3. Prohibition on the use of biometric surveillance by U.S. Immigration and Customs Enforcement or U.S. Customs and Border Protection\n##### (a) In general\nIt shall be unlawful for any covered immigration officer to acquire, possess, access, or use in the United States\u2014\n**(1)**\nany biometric surveillance system; or\n**(2)**\ninformation derived from a biometric surveillance system operated by another entity.\n##### (b) Biometric data deletion\nAll information collected by a covered immigration officer for use in, or derived from, a biometric surveillance system, including information collected before the date of the enactment of this Act, shall be deleted not later than 30 days after the date of the enactment of this Act.\n##### (c) Judicial investigations and proceedings\n**(1) Admissibility**\nExcept in a judicial investigation or proceeding alleging a violation of this section, information obtained in violation of this section is not admissible by the Federal Government in any criminal, civil, administrative, or other investigation or proceeding.\n**(2) Cause of action**\n**(A) In general**\nA violation of this section constitutes an injury to any individual aggrieved by such violation.\n**(B) Right to sue**\nAn individual aggrieved by a violation of this section may institute proceedings against the Federal Government whose covered immigration officer is alleged to have violated this section for the relief described in subparagraph (D) in any court of competent jurisdiction.\n**(C) Enforcement by state attorneys general**\nThe chief law enforcement officer of a State, or any other State officer authorized by law to bring actions on behalf of the residents of a State, may bring a civil action, as parens patriae, on behalf of the residents of such State in an appropriate district court of the United States to enforce this Act, whenever the chief law enforcement officer or other State officer determines the interests of the residents of such State have been or are being threatened or adversely affected by a violation of this section.\n**(D) Relief**\nIn a civil action authorized under subparagraph (B) in which the plaintiff prevails, the court may award\u2014\n**(i)**\nactual damages;\n**(ii)**\npunitive damages;\n**(iii)**\nreasonable attorneys\u2019 fees and costs; and\n**(iv)**\nany other relief, including injunctive relief, that the court determines to be appropriate.\n##### (d) Civil penalties\nAny covered immigration officer who violates this section may be subject to retraining, suspension, termination, or any other penalty, as determined in an appropriate tribunal, and subject to applicable due process requirements.\n##### (e) Rule of construction\nNothing in this section may be construed to preempt or supersede any Federal, State, or local law absent actual conflict with the limitations on covered immigration officers imposed by this section.",
      "versionDate": "2026-02-04",
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
        "actionDate": "2026-02-04",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3779",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ICE Out of Our Faces Act",
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
        "name": "Immigration",
        "updateDate": "2026-02-20T14:56:40Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7363ih.xml"
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
      "title": "ICE Out of Our Faces Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ICE Out of Our Faces Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the Department of Homeland Security's use of facial recognition.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:53Z"
    }
  ]
}
```
