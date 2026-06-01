# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6595?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6595
- Title: To direct the Secretary of Defense and the Secretary of Veterans Affairs to improve the availability of care for veterans at facilities of the Department of Defense.
- Congress: 119
- Bill type: HR
- Bill number: 6595
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-15T07:00:33Z
- Update date including text: 2026-01-15T07:00:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-10 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-18 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6595",
    "number": "6595",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001228",
        "district": "2",
        "firstName": "Derek",
        "fullName": "Rep. Schmidt, Derek [R-KS-2]",
        "lastName": "Schmidt",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "To direct the Secretary of Defense and the Secretary of Veterans Affairs to improve the availability of care for veterans at facilities of the Department of Defense.",
    "type": "HR",
    "updateDate": "2026-01-15T07:00:33Z",
    "updateDateIncludingText": "2026-01-15T07:00:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-18T14:09:33Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-10T15:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6595ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6595\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Schmidt (for himself and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Defense and the Secretary of Veterans Affairs to improve the availability of care for veterans at facilities of the Department of Defense.\n#### 1. Improvement of availability of care for veterans from facilities and providers of the Department of Defense\n##### (a) Action plans\n**(1) In general**\nPursuant to the authorities under section 8111 of title 38, United States Code, and section 1104 of title 10, United States Code, the Secretary of Defense and the Secretary of Veterans Affairs shall develop and implement action plans at covered facilities\u2014\n**(A)**\nto strengthen sharing of resources between the Department of Defense and the Department of Veterans Affairs under existing statutory authority;\n**(B)**\nto improve communication between the Department of Veterans Affairs and pertinent command and director leadership of military medical treatment facilities;\n**(C)**\nto increase utilization of military medical treatment facilities with excess capacity or space;\n**(D)**\nto increase case volume and complexity for graduate professional and other medical education programs of the Department of Defense and the Department of Veterans Affairs; and\n**(E)**\nto increase access to care for enrolled veterans in areas in which a military medical treatment facility is located that is identified by the Secretary of Defense as having excess capacity or space.\n**(2) Matters to be included**\nThe action plans required under paragraph (1) shall include the following:\n**(A)**\nCross-credentialing and privileging of health care providers to jointly care for enrolled veterans in medical facilities of the Department of Defense and the Department of Veterans Affairs.\n**(B)**\nExpedited access to installations of the Department of Defense for staff of the Department of Veterans Affairs and enrolled veterans.\n**(C)**\nThe designation of a coordinator within each covered facility to serve as a liaison between the Department of Defense and the Department of Veterans Affairs and to lead the implementation of such action plan.\n**(D)**\nA mechanism for monitoring the effectiveness of such action plan on an ongoing basis, to include establishing relevant performance goals and collecting data to assess progress towards those goals.\n**(E)**\nPrioritized integration of relevant information technology and other systems or processes to enable seamless information sharing, medical records referrals and ancillary orders and results, payment methodologies and billing processes, and workload attribution when personnel of the Department of Veterans Affairs provide services at facilities of the Department of Defense or when personnel of the Department of Defense provide services at facilities of the Department of Veterans Affairs.\n**(F)**\nAn oversight and accountability plan for the handling of adverse medical events and complaints from patients or staff, including a requirement to track any significant adverse medical events and provide information on such events in the briefing required under subsection (f).\n**(G)**\nAny other matter that the Secretary of Defense and the Secretary of Veterans Affairs consider appropriate.\n##### (b) Approval of action plans\nBefore any action plan required under subsection (a) with respect to a covered facility shall be considered complete and submitted to the appropriate committees of Congress pursuant to subsection (e), the Secretary of Defense and the Secretary of Veterans Affairs shall ensure that approval for the action plan is obtained from\u2014\n**(1)**\nthe co-chairs of the Department of Veterans Affairs-Department of Defense Joint Executive Committee established under section 320 of title 38, United States Code;\n**(2)**\nthe local installation commander for the covered facility of the Department of Defense; and\n**(3)**\nthe director of the relevant medical center of the Department of Veterans Affairs with respect to any covered facility of the Department of Veterans Affairs.\n##### (c) Requirements relating to sharing agreements\n**(1) Lead coordinator**\nThe Secretary of Defense and the Secretary of Veterans Affairs shall ensure that there is a lead coordinator at each facility of the Department of Defense or the Department of Veterans Affairs, as the case may be, with respect to which there is a sharing agreement in place.\n**(2) List of agreements**\nThe Secretary of Defense and the Secretary of Veterans Affairs shall maintain on a publicly available website a list of the sharing agreements in place between the medical facilities of the Department of Defense and the Department of Veterans Affairs.\n##### (d) Patient safety, complaints, and accountability\n**(1) Secure complaint process**\n**(A) In general**\nThe Secretary of Defense and the Secretary of Veterans Affairs shall establish a secure mechanism for enrolled veterans to report concerns regarding care received under an action plan required under subsection (a).\n**(B) Elements of mechanism**\nThe mechanism established under subparagraph (A) shall protect confidentiality, prohibit retaliation, and ensure transmission of each complaint to both the Department of Defense and the Department of Veterans Affairs.\n**(2) Documentation and review**\n**(A) Documentation**\nThe Secretary of Defense and the Secretary of Veterans Affairs shall maintain records of all complaints, adverse events, and safety incidents involving patients or staff pursuant to the action plans required by subsection (a).\n**(B) Review**\nThe records maintained under subparagraph (A) shall be jointly reviewed on a quarterly basis by designated officials of the Department of Defense and the Department of Veterans Affairs.\n**(3) Notification and investigation**\nAny allegation of abuse, neglect, or misconduct involving personnel of the Department of Defense in the treatment of a veteran under an action plan shall be promptly referred by the Secretary of Veterans Affairs, the Secretary of Defense, and the commander or medical center director, as applicable, of the facility concerned to the Office of Inspector General of the Department of Defense and the Department of Veterans Affairs.\n**(4) Interim protective measures**\nPending resolution of any investigation relating to conduct under an action plan, the Secretary of Veterans Affairs may suspend referrals of veterans to the provider or facility concerned.\n##### (e) Submission to Congress\nNot later than 30 days following the completion of the action plans required under subsection (a), the Secretary of Defense and the Secretary of Veterans Affairs shall submit such plans to the appropriate committees of Congress.\n##### (f) Annual joint briefings on action plans\nNot later than one year after submitting the action plans to the appropriate committees of Congress pursuant to subsection (e), the Secretary of Defense and the Secretary of Veterans Affairs shall provide to the appropriate committees of Congress a briefing containing\u2014\n**(1)**\na status update on the progress of implementing the action plans required under this section;\n**(2)**\nrecommendations for developing subsequent action plans for each facility with respect to which there is a sharing agreement in place;\n**(3)**\nthe number of patients served pursuant to the action plans, broken down by facility and service type;\n**(4)**\nthe number of health care providers who were cross-credentialed or privileged to jointly care for beneficiaries in medical facilities of the Department of Defense or the Department of Veterans Affairs pursuant to the action plans, broken down by facility and service type;\n**(5)**\nthe costs incurred and reimbursed between the Department of Defense and the Department of Veterans Affairs pursuant to the action plans, including an accounting of the use of the DOD\u2013VA Health Care Sharing Incentive Fund established under section 8111(d)(2) of title 38, United States Code, if applicable;\n**(6)**\na summary of the effectiveness of the mechanisms developed pursuant to the action plans related to oversight, accountability, data-gathering, and performance goals as well as any recommendations for improving such mechanisms;\n**(7)**\na summary of any patient safety incidents or complaints and associated resolutions as well as any recommendations for improving the patient safety and complaint resolution process under the actions plans; and\n**(8)**\na summary of the integration of information technology and other systems pursuant to the action plans as well as barriers to further integration and recommendations for improving such integration.\n##### (g) Rule of construction\nNothing in this section shall be construed to allow the Department of Defense or the Department of Veterans Affairs to require a veteran to seek care at a facility of the Department of Defense or to allow military medical treatment facilities to be used as a facility of the Department of Veterans Affairs for purposes of determining eligibility of veterans for care from a non-Department of Veterans Affairs provider under the eligibility access standards developed under section 1703B of title 38, United States Code.\n##### (h) Sunset\nThis section shall terminate on September 30, 2028.\n##### (i) Definitions\nIn this section:\n**(1)**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the Senate; and\n**(B)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(2)**\nThe term covered facility means\u2014\n**(A)**\na military medical treatment facility (as such term is defined in section 1073c of title 10, United States Code); or\n**(B)**\na medical facility of the Department of Veterans Affairs described in section 8101(3) of title 38, United States Code.\n**(3)**\nThe term enrolled veteran means a veteran enrolled in the patient enrollment system of the Department of Veterans Affairs established and operated under section 1705(a) of title 38, United States Code.\n**(4)**\nThe term sharing agreement means an agreement for the sharing of health-care resources between the Department of Defense and the Department of Veterans Affairs under section 1104 of title 10, United States Code, or section 8111 of title 38, United States Code.\n**(5)**\nThe term veteran has the meaning given that term in section 101 of title 38, United States Code.",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-08",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3388",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SERVE Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-11T15:26:45Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6595ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense and the Secretary of Veterans Affairs to improve the availability of care for veterans at facilities of the Department of Defense.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T14:05:36Z"
    },
    {
      "title": "To direct the Secretary of Defense and the Secretary of Veterans Affairs to improve the availability of care for veterans at facilities of the Department of Defense.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T09:07:32Z"
    }
  ]
}
```
