# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5247
- Title: To provide for the International Security Affairs authorities of the Department of State.
- Congress: 119
- Bill type: HR
- Bill number: 5247
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-12-15T21:48:36Z
- Update date including text: 2025-12-15T21:48:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 19.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 19.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5247",
    "number": "5247",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To provide for the International Security Affairs authorities of the Department of State.",
    "type": "HR",
    "updateDate": "2025-12-15T21:48:36Z",
    "updateDateIncludingText": "2025-12-15T21:48:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
        "item": [
          {
            "date": "2025-09-18T18:16:52Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-17T18:16:44Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-10T14:06:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5247ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5247\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Self introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for the International Security Affairs authorities of the Department of State.\nIV\nInternational Security Affairs\n#### 401. Under Secretary for International Security Affairs\n##### (a) Establishment\nThere shall be in the Department an Under Secretary for International Security Affairs who shall be responsible to the Secretary for matters pertaining to international security policy and assistance, arms control, nonproliferation, disarmament, nuclear weapons policy, international counterterrorism, transnational organized crime, international narcotics control, emerging threats, political-military affairs, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Under Secretary of State for International Security Affairs shall maintain continuous observation and coordination of all matters pertaining to international security in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nDeveloping policies for consideration by the Secretary and Deputy Secretary related to international security policy, including, as appropriate\u2014\n**(A)**\nin the areas of nonproliferation, arms control, strategic export controls, regional security and defense relations;\n**(B)**\nUnited States military-related activities with foreign policy implications; and\n**(C)**\narms transfers, security assistance, international counterterrorism, transnational organized crime, international narcotics controls, and other related matters.\n**(2)**\nLeading engagements with other agencies of the United States Government and in bilateral and multilateral engagements related to such matters as described in this section.\n**(3)**\nProviding guidance to Department personnel in the United States and overseas who conduct or implement policies, programs, and activities related to matters described in this section.\n#### 402. Office to monitor and combat trafficking\n##### (a) In general\n**(1) Establishment**\nThe Secretary shall establish within the Department an Office to Monitor and Combat Trafficking, which shall provide assistance to the Interagency Task Force to Monitor and Combat Trafficking and shall report directly to the Under Secretary for International Security Affairs for matters relating to day-to-day administration and coordination of activities and programs. Any such Office shall be headed by a Director, who shall be appointed by the President, by and with the advice and consent of the Senate, with the rank of Ambassador-at-Large, and shall have two deputy directors. The Director shall report to the Secretary and shall have the primary responsibility for assisting the Secretary in carrying out the purposes of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7101 et seq. ) and may have additional responsibilities as determined by the Secretary. The Director shall consult with nongovernmental organizations and multilateral organizations, and with trafficking victims or other affected persons. The Director shall have the authority to take evidence in public hearings or by other means.\n**(2) Staff**\nThe heads of each of the Federal departments and agencies represented on the Interagency Task Force to Monitor and Combat Trafficking are authorized to provide staff to the Office on a non-reimbursable basis.\n##### (b) United States assistance\nThe Director shall additionally be responsible for\u2014\n**(1)**\nall policy, funding, and programming decisions regarding funds made available for trafficking in persons programs that are centrally controlled by the Office to Monitor and Combat Trafficking;\n**(2)**\ncoordinating any trafficking in persons programs of the Department or of other Federal Government agencies;\n**(3)**\ncompiling, drafting, and coordinating the production and issuing of the annual report;\n**(4)**\nensuring, in coordination with other relevant officials, that all Department staff have completed annual anti-trafficking training pursuant to section 107(c)(4) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7105(c)(4) ) and section 708(a) of the Foreign Service Act of 1980 ( 22 U.S.C. 4028(a) );\n**(5)**\nencouraging the inclusion in country and regional planning of a counter-trafficking in persons analytic component to guide foreign assistance program design and implementation and to inform diplomatic engagement pursuant to section 105(f) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7103(f) ); and\n**(6)**\norganizing and coordinating the Trafficking in Persons Report Heroes Award.\n#### 403. Authorization of Appropriations for International Security Affairs\nOf the funds authorized to be appropriated to the Secretary of State under section 141, the Under Secretary for International Security Affairs shall receive the funds necessary to fulfill the Under Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 404. Assistant Secretary for Political-Military Affairs\nThere is authorized to be in the Department an Assistant Secretary for Political-Military Affairs who shall be responsible to the Under Secretary for International Security Affairs for matters pertaining to coordination with the Department of Defense or foreign militaries, and such other related duties as the Secretary may from time to time designate.\n#### 405. Authorization of Appropriations for Political-Military Affairs\n##### (a) Administration of accounts\nThe Assistant Secretary for Political-Military Affairs shall direct, oversee, and otherwise exercise responsibility of funds made available for\u2014\n**(1)**\ninternational military education and training; and\n**(2)**\nthe national security engagement account.\n##### (b) Authorization of appropriations\nOf the funds authorized to be appropriated to the Under Secretary for International Security Affairs under section 403, the Assistant Secretary for Political-Military Affairs shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 406. Assistant Secretary for International Narcotics and Law Enforcement Affairs\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for International Narcotics and Law Enforcement Affairs who shall be responsible to the Under Secretary for International Security Affairs for matters pertaining to international narcotics, anti-crime, and law enforcement affairs, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for International Narcotics and Law Enforcement Affairs shall maintain continuous observation and coordination of all matters pertaining to narcotics, transnational crime, and law enforcement affairs in the conduct of foreign policy by the Department, including, as appropriate, the following:\n**(1)**\nLeading the coordination of programs carried out by United States Government agencies abroad.\n**(2)**\nOverall supervision of policy and resources of international narcotics, anti-crime, and law enforcement activities.\n**(3)**\nCombating international narcotics production and trafficking, including by carrying out relevant delegated responsibilities under chapter 8 of part I of the Foreign Assistance Act of 1961.\n**(4)**\nStrengthening foreign justice systems, including judicial and prosecutorial capacity, appeals systems, law enforcement agencies, prison systems, and the sharing of recovered assets, for the purposes of investigating, prosecuting, and litigating criminal cases related to illicit narcotics production and trafficking and transnational organized crime.\n**(5)**\nTraining and equipping foreign police, border control, other government officials, and other civilian law enforcement authorities for anti-crime purposes, including ensuring that no foreign security unit or member of such unit shall receive such assistance from the United States Government absent appropriate vetting.\n**(6)**\nCombatting all forms of transnational organized crime, including human trafficking, illicit trafficking in arms and cultural property, migrant smuggling and facilitating illegal immigration for profit, corruption, money laundering, the illicit smuggling of bulk cash, other forms of illicit finance, the licit use of financial systems for malign purposes, and other new and emerging forms of crime.\n**(7)**\nIdentifying and responding to global corruption in accordance with United States national security interests and foreign policy objectives, including strengthening the capacity of foreign government institutions responsible for addressing financial crimes.\n**(8)**\nCoordinating with the Office of National Drug Control Policy to ensure lessons learned from other Federal departments and agencies are available to the Bureau of International Narcotics and Law Enforcement Affairs of the Department.\n**(9)**\nDeveloping standard requirements for monitoring and evaluation of Bureau programs, including metrics for success that do not rely solely on the amounts of illegal drugs that are produced or seized.\n**(10)**\nCarrying out timely and substantive consultation with chiefs of mission and, as appropriate, the heads of other United States Government agencies to ensure effective coordination of all international narcotics and law enforcement programs carried out overseas by the Department and such other agencies.\n**(11)**\nIn coordination with the Under Secretary for International Security Affairs, annually certifying in writing to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that United States enforcement personnel posted abroad whose activities are funded to any extent by the Bureau of International Narcotics and Law Enforcement Affairs are complying with section 207 of the Foreign Service Act of 1980 ( 22 U.S.C. 3927 ).\n**(12)**\nPerforming such other duties as the Under Secretary for International Security Affairs may from time to time designate.\n#### 407. Bureau of International Narcotics and Law Enforcement Affairs\n##### (a) Establishment\nThe Secretary shall establish a Bureau of International Narcotics and Law Enforcement Affairs, which shall perform such functions related to international narcotics, anti-crime, law enforcement, and transnational crime as the Under Secretary for International Security Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for International Narcotics and Law Enforcement Affairs shall be the head of the Bureau of International Narcotics and Law Enforcement Affairs.\n#### 408. Authorization of Appropriations for International Narcotics and Law Enforcement Affairs\n##### (a) Administration of accounts\nThe Assistant Secretary for International Narcotics and Law Enforcement Affairs shall direct, oversee, and otherwise exercise responsibility of funds made available for international narcotics control and law enforcement.\n##### (b) Authorization of appropriations\nOf the funds authorized to be appropriated to the Under Secretary for International Security Affairs under section 403, the Assistant Secretary for International Narcotics and Law Enforcement Affairs shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 409. Bureau of Arms Control and Nonproliferation\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Arms Control and Nonproliferation, which shall perform such functions related to verification and compliance with international arms control, nonproliferation, disarmament agreements or commitments, and other related international security policy issues, as the Under Secretary for International Security Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for Arms Control and Nonproliferation shall be the head of the Bureau of Arms Control and Nonproliferation.\n#### 410. Assistant Secretary for Counterterrorism\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Counterterrorism who shall be responsible to the Under Secretary for International Security Affairs for matters pertaining to international counterterrorism activities and programs and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for Counterterrorism shall maintain continuous observation and coordination of all matters pertaining to international counterterrorism matters in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nOverall supervision, including policy oversight of resources, of international counterterrorism activities.\n**(2)**\nServing as the principal policy advisor to the Secretary regarding international counterterrorism matters.\n**(3)**\nRepresenting the Secretary on international counterterrorism issues in international and interagency meetings, as appropriate.\n**(4)**\nCountering, in conjunction with other relevant bureaus of the Department and other Federal departments and agencies, all forms of international terrorism.\n**(5)**\nLeading United States foreign policy for counterterrorism efforts, including cooperation, coordination, and assistance that advances the interest, safety, and economic prosperity of the American people.\n**(6)**\nPerforming such other duties as the Under Secretary for International Security Affairs may from time to time designate.\n#### 411. Authorization of Appropriations for Counterterrorism\nOf the funds authorized to be appropriated to the Under Secretary for International Security Affairs under section 403, the Assistant Secretary for Counterterrorism shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 412. Assistant Secretary for Emerging Threats\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Emerging Threats who shall be responsible to the Under Secretary for International Security Affairs for matters pertaining to emerging security threats and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for Emerging Threats shall maintain continuous observation and coordination of all matters pertaining to emerging security threats in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nServing as the principal emerging security threats official within the senior management of the Department and as the advisor to the Secretary for emerging security threats, including with respect to lethal autonomous systems, engineered bioweapons, and emerging uses of artificial intelligence, biotechnology, quantum information science, and emerging foundational technologies.\n**(2)**\nMitigating threats resulting from military applications of emerging technologies, including in the fields of artificial intelligence, biotechnology, and quantum information science, in support of United States foreign policy and national security.\n**(3)**\nLeading engagement, in coordination with relevant executive branch agencies, on development of diplomatic policy for national security related activities and emerging threats in the polar regions, outer space, and undersea domains.\n**(4)**\nLeading engagement, in coordination with relevant executive branch agencies, on the development of diplomatic policy for quantum information science, including in the field of quantum cryptography, navigation and timing, spectrum, imaging, and detection; sensors and computing.\n**(5)**\nPerforming such other duties as the Under Secretary for International Security Affairs may from time to time designate.\n#### 413. Bureau of Emerging Threats\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Emerging Threats, which shall perform such functions related to emerging security threats, including with respect to lethal autonomous systems, engineered bioweapons, military application of cyberspace operations, undersea and outer space domains, emerging and foundational technologies, associated security issues in polar regions, and emerging uses of artificial intelligence, biotechnology, quantum information science, as the Under Secretary for International Security Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for Emerging Threats shall be the head of the Bureau of Emerging Threats.\n#### 414. Authorization of appropriations for emerging threats\nOf the funds authorized to be appropriated to the Under Secretary for International Security Affairs under section 403, the Assistant Secretary for Emerging Threats shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 415. References\nAny reference in any statute, reorganization plan, Executive order, regulation, agreement, determination, or other official document or proceeding to\u2014\n**(1)**\nthe Under Secretary for Arms Control and International Security Affairs shall be deemed to refer to the Under Secretary for International Security Affairs;\n**(2)**\nthe Under Secretary for Security Assistance, Science, and Technology shall be deemed to refer to the Under Secretary for International Security Affairs;\n**(3)**\nthe Under Secretary for Security Assistance shall be deemed to refer to the Under Secretary for International Security;\n**(4)**\nthe Assistant Secretary for Arms Control, Deterrence, and Stability shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(5)**\nthe Assistant Secretary for Arms Control, Verification, and Stability shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(6)**\nthe Assistant Secretary for Verification, Compliance, and Implementation shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(7)**\nthe Assistant Secretary for Verification and Compliance shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(8)**\nthe Assistant Secretary for International Security and Nonproliferation shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(9)**\nthe Assistant Secretary for Nonproliferation shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(10)**\nthe Assistant Secretary for Nonproliferation shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(11)**\nthe Assistant Secretary for Arms Control shall be deemed to refer to the Assistant Secretary for Arms Control and Nonproliferation;\n**(12)**\nthe Bureau for Arms Control, Deterrence, and Stability shall be deemed to refer to the Bureau for Arms Control and Nonproliferation;\n**(13)**\nthe Bureau for Arms Control, Verification, and Stability shall be deemed to refer to the Bureau for Arms Control and Nonproliferation;\n**(14)**\nthe Bureau for Verification, Compliance, and Implementation shall be deemed to refer to the Bureau for Arms Control and Nonproliferation;\n**(15)**\nthe Bureau for Verification and Compliance shall be deemed to refer to the Bureau for Arms Control and Nonproliferation;\n**(16)**\nthe Bureau for International Security and Nonproliferation shall be deemed to refer to the Bureau for Arms Control and Nonproliferation;\n**(17)**\nthe Bureau for Nonproliferation shall be deemed to refer to the Bureau for Arms Control and Nonproliferation; and\n**(18)**\nthe Bureau for Arms Control shall be deemed to refer to the Bureau for Arms Control and Nonproliferation.\n#### 416. Classification to United States Code\nThe Office of Law Revision Counsel is directed to\u2014\n**(1)**\nutilize sections 98\u2013128 of title 22, United States Code, to classify the sections of this title; and\n**(2)**\nmaintain the legislative history, under editorial notes, of repealed law which previously occupied the corresponding sections of United States Code.",
      "versionDate": "2025-09-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-12-15T21:48:36Z"
          },
          {
            "name": "Arms control and nonproliferation",
            "updateDate": "2025-12-15T21:47:17Z"
          },
          {
            "name": "Department of State",
            "updateDate": "2025-12-15T21:46:40Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-15T21:47:05Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-12-15T21:47:53Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-12-15T21:46:49Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-12-15T21:46:55Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-12-15T21:48:13Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-12-15T21:48:28Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2025-12-15T21:48:02Z"
          },
          {
            "name": "Nuclear weapons",
            "updateDate": "2025-12-15T21:47:22Z"
          },
          {
            "name": "Organized crime",
            "updateDate": "2025-12-15T21:47:37Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-12-15T21:48:19Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2025-12-15T21:47:30Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-12-15T21:47:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-11T21:38:46Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5247ih.xml"
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
      "title": "To provide for the International Security Affairs authorities of the Department of State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T10:18:25Z"
    },
    {
      "title": "To provide for the International Security Affairs authorities of the Department of State.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:14Z"
    }
  ]
}
```
