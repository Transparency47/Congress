# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1744?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1744
- Title: PORCUPINE Act
- Congress: 119
- Bill type: S
- Bill number: 1744
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2026-02-11T14:26:38Z
- Update date including text: 2026-02-11T14:26:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 232.
- 2025-12-11 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8693; text of amendment in the nature of a substitute: CR S8693)
- 2025-12-11 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-15 - Floor: Message on Senate action sent to the House.
- 2025-12-15 16:06:17 - Floor: Received in the House.
- 2025-12-15 16:19:16 - Floor: Held at the desk.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 232.
- 2025-12-11 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8693; text of amendment in the nature of a substitute: CR S8693)
- 2025-12-11 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-15 - Floor: Message on Senate action sent to the House.
- 2025-12-15 16:06:17 - Floor: Received in the House.
- 2025-12-15 16:19:16 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1744",
    "number": "1744",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "PORCUPINE Act",
    "type": "S",
    "updateDate": "2026-02-11T14:26:38Z",
    "updateDateIncludingText": "2026-02-11T14:26:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-15",
      "actionTime": "16:19:16",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-15",
      "actionTime": "16:06:17",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8693; text of amendment in the nature of a substitute: CR S8693)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 232.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-13",
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
            "date": "2025-10-30T15:05:48Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:35Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-13T21:04:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "DE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CO"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "FL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1744is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1744\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Ricketts (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Arms Export Control Act to include Taiwan among the list of recipient countries with respect to which shorter certification and reporting periods apply and to expedite licensing for allies transferring military equipment to Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act or PORCUPINE Act .\n#### 2. Modification of certification and reporting requirements under the Arms Export Control Act\nThe Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) is amended\u2014\n**(1)**\nin section 3 ( 22 U.S.C. 2753 )\u2014\n**(A)**\nin subsection (b)(2), by inserting the Government of Taiwan, before or the ; and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (2)(B), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (3)(A)(i), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(2)**\nin section 21 ( 22 U.S.C. 2761 )\u2014\n**(A)**\nin subsection (e)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(B)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (1)(A), by striking or Israel and inserting Israel, or Taiwan ; and\n**(ii)**\nin paragraph (2), by striking or Israel and inserting Israel, or Taiwan ;\n**(3)**\nin section 36 ( 22 U.S.C. 2776 )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), in the undesignated matter following subparagraph (P), in the second sentence, by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (2), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(ii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(C)**\nin subsection (d)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(4)**\nin section 62(c)(1) ( 22 U.S.C. 2796a(c)(1) ), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(5)**\nin section 63(a)(2) ( 22 U.S.C. 2796b(a)(2) ), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan .\n#### 3. Expedited licensing for allies transferring military equipment to Taiwan\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall establish an expedited decision-making process for blanket third party transfers of defense articles and services from North Atlantic Treaty Organization member countries, Japan, Australia, the Republic of Korea, Israel, or New Zealand to Taiwan, including transfers and re-transfers of United States origin grant, Foreign Military Sales, and Direct Commercial Sales end-items not covered by an exemption under the International Traffic in Arms Regulations under subchapter M of chapter I of title 22, Code of Federal Regulations.\n##### (b) Availability\nThe expedited decision-making process described in subsection (a)\u2014\n**(1)**\nshall be available for classified and unclassified items; and\n**(2)**\nshall, to the extent practicable\u2014\n**(A)**\nrequire the approval, return, or denial of any licensing application to export defense articles and services that is related to a government-to-government agreement within 15 days after the submission of such application; and\n**(B)**\nrequire the completion of the review of all other licensing requests not later than 30 days after the submission of such application.\n##### (c) Report\nNot later than 1 year after the date on which the expedited decision-making process under subsection (a) is established, the Secretary of State shall submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report on the implementation and effectiveness of such process, including an assessment of the actions taken to coordinate with North Atlantic Treaty Organization member countries, Japan, Australia, the Republic of Korea, Israel, and New Zealand to ensure alignment with the respective export control regulations of such countries.",
      "versionDate": "2025-05-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1744rs.xml",
      "text": "II\nCalendar No. 232\n119th CONGRESS\n1st Session\nS. 1744\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Ricketts (for himself, Mr. Coons , Mr. Cornyn , Mr. Bennet , Mr. Budd , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend the Arms Export Control Act to include Taiwan among the list of recipient countries with respect to which shorter certification and reporting periods apply and to expedite licensing for allies transferring military equipment to Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act or PORCUPINE Act .\n#### 2. Modification of certification and reporting requirements under the Arms Export Control Act\nThe Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) is amended\u2014\n**(1)**\nin section 3 ( 22 U.S.C. 2753 )\u2014\n**(A)**\nin subsection (b)(2), by inserting the Government of Taiwan, before or the ; and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (2)(B), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (3)(A)(i), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(2)**\nin section 21 ( 22 U.S.C. 2761 )\u2014\n**(A)**\nin subsection (e)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(B)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (1)(A), by striking or Israel and inserting Israel, or Taiwan ; and\n**(ii)**\nin paragraph (2), by striking or Israel and inserting Israel, or Taiwan ;\n**(3)**\nin section 36 ( 22 U.S.C. 2776 )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), in the undesignated matter following subparagraph (P), in the second sentence, by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (2), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(ii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(C)**\nin subsection (d)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(4)**\nin section 62(c)(1) ( 22 U.S.C. 2796a(c)(1) ), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(5)**\nin section 63(a)(2) ( 22 U.S.C. 2796b(a)(2) ), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan .\n#### 3. Expedited licensing for allies transferring military equipment to Taiwan\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall establish an expedited decision-making process for blanket third party transfers of defense articles and services from North Atlantic Treaty Organization member countries, Japan, Australia, the Republic of Korea, Israel, or New Zealand to Taiwan, including transfers and re-transfers of United States origin grant, Foreign Military Sales, and Direct Commercial Sales end-items not covered by an exemption under the International Traffic in Arms Regulations under subchapter M of chapter I of title 22, Code of Federal Regulations.\n##### (b) Availability\nThe expedited decision-making process described in subsection (a)\u2014\n**(1)**\nshall be available for classified and unclassified items; and\n**(2)**\nshall, to the extent practicable\u2014\n**(A)**\nrequire the approval, return, or denial of any licensing application to export defense articles and services that is related to a government-to-government agreement within 15 days after the submission of such application; and\n**(B)**\nrequire the completion of the review of all other licensing requests not later than 30 days after the submission of such application.\n##### (c) Report\nNot later than 1 year after the date on which the expedited decision-making process under subsection (a) is established, the Secretary of State shall submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report on the implementation and effectiveness of such process, including an assessment of the actions taken to coordinate with North Atlantic Treaty Organization member countries, Japan, Australia, the Republic of Korea, Israel, and New Zealand to ensure alignment with the respective export control regulations of such countries.",
      "versionDate": "2025-10-30",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1744es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1744\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Arms Export Control Act to include Taiwan among the list of recipient countries with respect to which shorter certification and reporting periods apply and to expedite licensing for allies transferring military equipment to Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act or PORCUPINE Act .\n#### 2. Modification of certification and reporting requirements under the Arms Export Control Act\n##### (a) In general\nThe Arms Export Control Act ( 22 U.S.C. 2751 et seq. ) is amended\u2014\n**(1)**\nin section 3 ( 22 U.S.C. 2753 )\u2014\n**(A)**\nin subsection (b)(2), by inserting Taiwan, before or the ; and\n**(B)**\nin subsection (d)\u2014\n**(i)**\nin paragraph (2)(B), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (3)(A)(i), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(2)**\nin section 21 ( 22 U.S.C. 2761 )\u2014\n**(A)**\nin subsection (e)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(B)**\nin subsection (h)\u2014\n**(i)**\nin paragraph (1)(A), by striking or Israel and inserting Israel, or Taiwan ; and\n**(ii)**\nin paragraph (2), by striking or Israel and inserting Israel, or Taiwan ;\n**(3)**\nin section 36 ( 22 U.S.C. 2776 )\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin paragraph (1), in the undesignated matter following subparagraph (P), in the second sentence, by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(ii)**\nin paragraph (2), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(iii)**\nin paragraph (6), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(B)**\nin subsection (c)\u2014\n**(i)**\nin paragraph (2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(ii)**\nin paragraph (5), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(C)**\nin subsection (d)(2)(A), by striking or New Zealand and inserting New Zealand, or Taiwan ;\n**(4)**\nin section 62(c)(1) ( 22 U.S.C. 2796a(c)(1) ), by striking or New Zealand and inserting New Zealand, or Taiwan ; and\n**(5)**\nin section 63(a)(2) ( 22 U.S.C. 2796b(a)(2) ), in the matter preceding subparagraph (A), by striking or New Zealand and inserting New Zealand, or Taiwan .\n##### (b) Report\nNot later than two years after the date of the enactment of this section, and every two years thereafter, the Secretary of State shall submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report on the implementation and effectiveness of the amendments made by this section.\n#### 3. Feasibility assessment of expedited licensing for allies transferring military equipment to Taiwan\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State shall conduct an assessment of the feasibility of establishing an expedited decision-making process for third party transfers of defense articles and services from North Atlantic Treaty Organization member countries, Japan, Australia, the Republic of Korea, New Zealand, or Israel to Taiwan, including transfers and re-transfers of United States-origin grant, Foreign Military Sales, and Direct Commercial Sales end-items not covered by an exemption under the International Traffic in Arms Regulations under subchapter M of chapter I of title 22, Code of Federal Regulations.\n##### (b) Elements\nThe assessment required by subsection (a) shall include an assessment of the following:\n**(1)**\nThe availability of such an expedited decision-making process for classified and unclassified items.\n**(2)**\nThe feasibility of requiring\u2014\n**(A)**\nthe approval, return, or denial of any licensing application to export defense articles and services that is related to a government-to-government agreement within 15 days after the submission of such application; and\n**(B)**\nthe completion of the review of all other licensing requests not later than 30 days after the submission of such application.\n##### (c) Briefing\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall provide the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives with a briefing on the outcome of the assessment required by subsection (a).\n#### 4. Rule of construction\nNothing in this Act may be construed to alter the policy of the United States toward Taiwan as specified in the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ).\n#### 5. Sunset\nThis Act shall cease to have effect on the date that is 7 years after the date of the enactment of this Act.",
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
        "actionDate": "2026-01-16",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "7146",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PORCUPINE Act",
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
            "name": "Asia",
            "updateDate": "2025-12-17T17:29:25Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-17T17:29:37Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-12-17T17:29:31Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2025-12-17T17:29:12Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2025-12-17T17:29:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-10T14:59:29Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1744is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1744rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1744es.xml"
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
      "title": "PORCUPINE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:03:15Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "PORCUPINE Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-12T06:08:16Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-12T06:08:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:38:13Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "PORCUPINE Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:38:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PORCUPINE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Our Regional Companions Upgraded Protection in Nefarious Environments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Arms Export Control Act to include Taiwan among the list of recipient countries with respect to which shorter certification and reporting periods apply and to expedite licensing for allies transferring military equipment to Taiwan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T03:33:19Z"
    }
  ]
}
```
