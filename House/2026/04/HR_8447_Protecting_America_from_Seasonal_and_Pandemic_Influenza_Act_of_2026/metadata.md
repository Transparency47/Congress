# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8447?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8447
- Title: Protecting America from Seasonal and Pandemic Influenza Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8447
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-05-21T16:31:14Z
- Update date including text: 2026-05-21T16:31:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8447",
    "number": "8447",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000560",
        "district": "2",
        "firstName": "Rick",
        "fullName": "Rep. Larsen, Rick [D-WA-2]",
        "lastName": "Larsen",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Protecting America from Seasonal and Pandemic Influenza Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T16:31:14Z",
    "updateDateIncludingText": "2026-05-21T16:31:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-22T15:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NC"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NM"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "DC"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8447ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8447\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Larsen of Washington (for himself, Ms. Ross , Ms. Stansbury , Ms. Norton , Ms. Barrag\u00e1n , and Mr. Thanedar ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo protect against seasonal and pandemic influenza, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting America from Seasonal and Pandemic Influenza Act of 2026 .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nInfluenza occurs seasonally each year, and throughout history, has caused devastating pandemics. The 1918 influenza pandemic killed an estimated 675,000 Americans.\n**(2)**\nIn an average season, influenza results in 6,300 to 52,000 deaths in the United States, including over 100 pediatric deaths. Additionally, influenza causes hundreds of thousands of hospitalizations and millions of illnesses.\n**(3)**\nThe Council of Economic Advisors issued a report in 2019 estimating that seasonal influenza costs the United States approximately $361,000,000,000 per year, and that an influenza pandemic has the potential to cause up to $3,790,000,000,000 in losses. This report was issued prior to the COVID\u201319 pandemic, which will cost the United States an estimated $16,000,000,000,000.\n**(4)**\nStrategies that increase seasonal influenza vaccination rates will also improve pandemic readiness.\n**(5)**\nThe National Influenza Vaccine Modernization Strategy of 2020\u20132030, established pursuant to Executive Order 13887, titled Modernizing Influenza Vaccines in the United States to Promote National Security and Public Health , should be fully implemented to ensure the Nation\u2019s vaccine enterprise is highly responsive, flexible, scalable, and effective at reducing the impact of seasonal and pandemic influenza viruses.\n**(6)**\nCritical United States pharmaceutical supply chains are dangerously reliant on China, and the United States must take actions to strengthen its position as the global leader in biotechnology research and development.\n**(7)**\nVaccine hesitancy in the United States represents a threat to the Nation\u2019s national security and public health. Efforts must be taken to restore trust and confidence in scientific data and public health messaging.\n**(8)**\nSupport for communication, outreach, and administration across public health and health care settings is critical to ensure awareness of and access to influenza vaccines, treatments, and medical countermeasures.\n#### 3. Strengthening and diversifying influenza vaccine, therapeutics, and diagnostics development, manufacturing, and supply chain\n##### (a) Timely delivery of first doses of finished influenza vaccine\n**(1) National goal**\nIt is a national goal for the United States, not later than 3 years after the date of enactment of this Act, to have the capacity to deliver first doses of finished influenza vaccine within 12 weeks of emergence of an influenza strain with pandemic potential.\n**(2) Plan**\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services, the Assistant Secretary for Preparedness and Response, and the Director of the Biomedical Advanced Research and Development Authority shall publish a plan to achieve the goal specified in paragraph (1).\n##### (b) Universal influenza vaccine\n**(1) National goal**\nIt is a national goal for the United States, not later than 10 years after the date of enactment of this Act, to have developed a universal influenza vaccine.\n**(2) Plan**\n**(A) Publication**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, the Director of the National Institutes of Health, and the Director of the Biomedical Advanced Research and Development Authority shall publish a plan to achieve the goal specified in paragraph (1) in partnership with vaccine manufacturers.\n**(B) Interim support**\nThe plan under subparagraph (A) shall include provisions, as necessary to achieve such goal, for support over the period of 5 years following the publication of such plan of the following:\n**(i)**\nIncremental vaccine efficacy improvements.\n**(ii)**\nThe research workforce.\n##### (c) Strengthening the vaccine supply chain\n**(1) In general**\nThe Secretary of Health and Human Services shall\u2014\n**(A)**\nestablish public-private partnerships to strengthen the domestic vaccine supply chain; and\n**(B)**\nevaluate the capabilities, capacity, and utilization of such partnerships, including by assessing and testing relevant logistical and interoperable technology with stakeholders in the supply chain.\n**(2) Domestic vaccine supply chain**\nFor purposes of this subsection, the term domestic vaccine supply chain includes the full domestic supply chain, including\u2014\n**(A)**\nproduction of ingredients and manufacturing and distribution of finished vaccines;\n**(B)**\nfill-finish capacity; and\n**(C)**\nthe supply chain of ancillary supplies such as needles and syringes.\n##### (d) National Influenza Vaccine Modernization Strategy\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\nfully implement the portions of the National Influenza Vaccine Modernization Strategy 2020\u20132030 that are within the authority of the Department of Health and Human Services to carry out (under other applicable provisions of law); and\n**(2)**\nby June 15 each calendar year through 2030, submit to the Congress a report on such implementation.\n##### (e) Assistant Secretary for Preparedness and Response\nSection 2811 of the Public Health Service Act ( 42 U.S.C. 300hh\u201310 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (3), by inserting , including the pandemic influenza medical countermeasures program under paragraphs (2)(E) and (4)(H) of section 319L(c) after qualified pandemic or epidemic products (as defined in section 319F\u20133) ; and\n**(B)**\nin paragraph (7), by inserting , including through the pandemic influenza medical countermeasures program under paragraphs (2)(E) and (4)(H) of section 319L(c) after for each such threat ; and\n**(2)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (J), by striking and at the end;\n**(B)**\nby redesignating subparagraph (K) as subparagraph (L); and\n**(C)**\nby inserting after subparagraph (J) the following:\n(K) evaluate progress with respect to implementing the National Influenza Vaccine Modernization Strategy, issued in June 2020, or any successor strategy; and .\n##### (f) Biomedical advanced research and development authority\n**(1) Preparedness activities**\nSection 319L(c) of the Public Health Service Act (42 U.S.C. 247d\u20137e(c)) is amended\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (C), by striking and at the end;\n**(ii)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end of the following:\n(E) supporting pandemic influenza countermeasure preparedness. ; and\n**(B)**\nin paragraph (4), by adding at the end of the following:\n(H) Pandemic influenza medical countermeasures program In carrying out paragraph (2)(E), the Secretary shall establish and implement a program that\u2014 (i) supports research and development activities for qualified pandemic or epidemic products (as defined in section 319F\u20133), including by\u2014 (I) developing innovative technologies to enhance rapid response to pandemic influenza threats; (II) developing influenza vaccines with potential universal vaccination capability; (III) developing influenza vaccines with longer lasting broad spectrum protective immunity against a wider range of antigenically divergent influenza strains; (IV) developing alternative vaccine delivery approaches; (V) developing novel small- and large-molecule novel influenza antivirals, monoclonal antibodies, and other products that provide better influenza treatment and prevention; (VI) developing innovative technologies to enhance rapid diagnosis of influenza; and (VII) implementing the National Influenza Vaccine Modernization Strategy, issued in June 2020, or any successor strategy; (ii) ensures readiness to respond to qualified pandemic and epidemic threats, including by\u2014 (I) supporting development and manufacturing of influenza virus seeds, clinical trial lots, and stockpiles of novel influenza strains; (II) supporting the stockpile of influenza antivirals through diversifying and replenishing the existing stockpile of influenza antivirals; (III) supporting manufacturing and fill-finish rapid response infrastructure; (IV) supporting the stockpile of influenza testing equipment and supplies; and (V) testing and evaluating pandemic threat rapid response capabilities through regular preparedness drills with key public and private sector partners that examine the range of activities (including production and clinical testing of influenza diagnostics, vaccines, and therapeutics) required to effectively respond to novel threats; and (iii) builds, sustains, and replenishes qualified pandemic and epidemic stockpiles of bulk antigen and adjuvant material, including by\u2014 (I) annually testing the potency and shelflife potential of all existing pandemic and epidemic stockpiles held by the Department of Health and Human Services; and (II) developing, and disseminating to key public and private sector partners, a life cycle management plan. .\n##### (g) Authorization of appropriations\nSection 319L(d) of the Public Health Service Act (42 U.S.C. 247d\u20137e(d)) is amended by adding at the end the following:\n(3) Pandemic influenza To carry out this section and section 2811 with respect to pandemic influenza, in addition to amounts authorized to be appropriated by paragraph (2) and any amounts authorized to be appropriated by section 2811, there is authorized to be appropriated $335,000,000 for each of the fiscal years 2027 through 2031, to remain available until expended. .\n#### 4. Promoting innovative approaches and use of new technologies to detect, prevent, and respond to influenza\n##### (a) Prioritizing influenza, influenza combination, and pathogen agnostic tools\n**(1) NIH**\nThe Director of the National Institutes of Health may conduct or support basic research prioritizing the development of\u2014\n**(A)**\nagnostic tools to detect influenza and other pathogens; and\n**(B)**\ntechnologies that automate sample preparation for such tools.\n**(2) BARDA**\nThe Director of the Biomedical Advanced Research and Development Authority may conduct or support advanced development of novel sequencing modalities prioritizing tools described in paragraph (1)(A) and technologies described in paragraph (1)(B).\n##### (b) Development of point-of-Care and self-Testing diagnostics\nThe Director of the Biomedical Advanced Research and Development Authority, in collaboration with the Director of the Centers for Disease Control and Prevention, the Director of the National Institutes of Health, and the Commissioner of Food and Drugs, may conduct or support development of rapid, accurate, easily accessible, self-administrable diagnostic tests that are readable at the point of care or at home.\n##### (c) Incorporating diagnostics supply chain resiliency into influenza pandemic planning\nThe Assistant Secretary for Preparedness and Response, in collaboration with the Commissioner of Food and Drugs, the Director of the Centers for Disease Control and Prevention, the Secretary of Commerce, and the Secretary of Transportation, shall\u2014\n**(1)**\nincorporate diagnostics supply chain resiliency into influenza pandemic planning that supports a health care system that tests to treat and bolsters testing and vaccine delivery supply chains; and\n**(2)**\nnot later than 1 year after the date of enactment of this Act, publish a plan for rapidly expanding public and private diagnostic testing capacity (including at clinical laboratories, at public health department laboratories, and by means of self-testing) in an influenza pandemic, including addressing transportation infrastructure, the need for sterilization, and sourcing critical raw materials, components, and parts.\n##### (d) Scaling Up prophylactic influenza antibody products that address gaps in coverage\nThe Director of the Biomedical Advanced Research and Development Authority may conduct or support preventive approaches, including those still in preclinical and clinical stages, to rapidly scale up preexposure prophylactic influenza antibody products that address influenza infection.\n##### (e) Modernizing potency assays\nThe Commissioner of Food and Drugs shall work with vaccine manufacturers to modernize potency assays across a variety of manufacturing technologies so as to reduce by 6 weeks the period required to first evaluate new vaccine candidates during a pandemic.\n##### (f) Improved influenza therapeutics\nThe Director of the Biomedical Advanced Research and Development Authority may conduct or support improved influenza therapeutics that\u2014\n**(1)**\nare more broadly protective; and\n**(2)**\nmeet the needs of high-risk and high-exposure patients.\n#### 5. Increasing influenza vaccine, therapeutics, and testing access and coverage across all populations\n##### (a) Annual report on public communication strategy\nThe Director of the Centers for Disease Control and Prevention shall submit an annual report to the Congress on the public communication strategy of the Centers to increase public confidence in the safety and effectiveness of vaccines.\n##### (b) Sense of Congress\nIt is the sense of Congress that the National Institutes of Health, the Director of the Centers for Disease Control and Prevention, the Secretary of Defense, the Secretary of Veterans Affairs, the Administrator of the Centers for Medicare & Medicaid Services, and the Commissioner of Food and Drugs should support research using large data sets from multiple sources of health data to further support and evaluate vaccine safety and effectiveness over multiple influenza seasons.\n##### (c) Addressing misinformation and disinformation\n**(1) In general**\nThe Secretary of Health and Human Services shall create partnerships to educate individuals about the safety and efficacy of influenza vaccines and the potential harms of influenza, particularly for unvaccinated individuals.\n**(2) Requirement**\nThe partnerships under paragraph (1) shall allow for dissemination of best practices and lessons learned between partnering organizations.\n**(3) Members**\nThe members of the partnerships under paragraph (1) shall include representatives of organizations with experience working with vulnerable populations, including\u2014\n**(A)**\nindividuals with chronic health conditions;\n**(B)**\nolder Americans;\n**(C)**\nparents of young children;\n**(D)**\npregnant women;\n**(E)**\nTribal communities;\n**(F)**\nracial and ethnic minorities; and\n**(G)**\nrural communities.\n**(4) Conferring with partnering organizations**\nThe Secretary of Health and Human Services shall confer with organizations represented in partnerships under paragraph (1)\u2014\n**(A)**\nin advance of each seasonal influenza season, on messaging and communications; and\n**(B)**\nat the end of each seasonal influenza season, on best practices and lessons learned.\n**(5) Report to Congress**\nNot later than one year after the date of enactment of this Act, the Secretary of Health and Human Services shall report to the Congress on the partnerships created, and activities conducted, under this section.\n##### (d) Communications public-Private partnership\n**(1) In general**\nNot later than six months after the date of enactment of this Act, the Secretary of Health and Human Services shall implement a targeted demonstration project that provides for the establishment of a communications public-private partnership initiative for increasing vaccine confidence.\n**(2) Requirements**\nThe demonstration project under paragraph (1) shall\u2014\n**(A)**\nbe implemented through an independent, nongovernmental, nonprofit entity;\n**(B)**\nfocus on individuals with chronic illness or other comorbidities who tend to have worse clinical outcomes from influenza (such as individuals with heart disease or diabetes, and racial and ethnic minorities);\n**(C)**\nsupport behavioral research around sources of vaccine hesitancy; and\n**(D)**\ndevelop and implement a targeted, multimodal communications campaign, using internet platforms, television, and nontraditional targeted social media and community outreach in an effort to reach individuals who may be especially vaccine hesitant.\n**(3) Report**\nNot later than six months after completion of the demonstration project under paragraph (1), the Secretary of Health and Human Services shall\u2014\n**(A)**\nprepare a report on the demonstration project, including an evaluation of the project\u2019s methods, findings, and results; and\n**(B)**\nmake such report publicly available on the website of the Department of Health and Human Services.\n##### (e) Incorporating health outreach into seasonal and pandemic influenza planning and response\nThe Director of the Centers for Disease Control and Prevention and the Assistant Secretary for Preparedness and Response shall\u2014\n**(1)**\nincorporate health outreach into the seasonal and pandemic influenza planning and response programs overseen by such officials; and\n**(2)**\ninclude in such programs strategies to reach rural communities, communities with lower socioeconomic status, racial and ethnic minorities, seniors, and individuals with disabilities, including addressing barriers to vaccinations, therapeutics, and diagnostics in the point-of-care and at-home, self-testing settings.\n##### (f) Expanding access to influenza treatment through a test-To-Treat demonstration program\n**(1) Demonstration project**\n**(A) In general**\nNot later than one year after the date of enactment of this Act, the Secretary of Health and Human Services shall initiate an influenza test-to-treat demonstration project.\n**(B) Length; locations**\nThis demonstration project under subparagraph (A) shall run for the length of one seasonal influenza season and be based in one or more of the following locations:\n**(i)**\nFacilities that serve vulnerable populations, such as populations who are in long-term care facilities, are 65 years of age or older, may have other medical conditions, and will be in unavoidable close contact with others.\n**(ii)**\nFederal health care facilities that serve at-risk and vulnerable communities, such as Indian Health Service clinics, federally qualified health centers (as defined in section 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) )), and facilities of the Department of Veterans Affairs.\n**(iii)**\nOther appropriate locations identified by the Secretary of Health and Human Services, in consultation with external stakeholder organizations, to test the operational feasibility and impact of influenza test-to-treat programs.\n**(2) Report**\nNot later than 6 months after completion of the demonstration project, the Secretary of Health and Human Services shall\u2014\n**(A)**\nprepare a report on the demonstration project under paragraph (1), including an evaluation of the project\u2019s methods, findings, and results; and\n**(B)**\nmake such report publicly available on the website of the Department of Health and Human Services.\n##### (g) Creating administration pathways\nThe Secretary of Health and Human Services may award grants to States to create administration pathways for pharmacy personnel to administer influenza vaccines, tests, and therapeutics, in order to increase vaccination, testing, and relevant treatment as needed for adults and children.\n##### (h) Strategic National Stockpile and security countermeasure procurements\n**(1) In general**\nThe Secretary of Health and Human Services shall incorporate into the Strategic National Stockpile under section 319F\u20132 of the Public Health Service Act ( 42 U.S.C. 247d\u20136b ) products needed to respond to pandemic influenza, including through\u2014\n**(A)**\ndynamic management of antivirals;\n**(B)**\nvendor-managed inventory of testing equipment and supplies;\n**(C)**\nreplenishment of aging antivirals, testing equipment, supplies, and other products; and\n**(D)**\ndiversification of stockpiled products.\n**(2) Medical countermeasures preparedness review**\nThe Assistant Secretary for Preparedness and Response shall incorporate into the annual Medical Countermeasures Preparedness Review under section 319F\u20132 of the Public Health Service ( 42 U.S.C. 247d\u20136b ) an assessment of the supplies available for an influenza pandemic, including replenishment of used and expired medical countermeasures and an assessment of existing State-level stockpiles.\n**(3) GAO study**\nThe Comptroller General of the United States shall conduct a study of existing State-level pandemic stockpiles, guidance provided by Strategic National Stockpile to State stockpiles, and the sufficiency of such guidance.\n##### (i) Monitoring and distributing influenza antiviral supplies\nThe Secretary of Health and Human Services shall\u2014\n**(1)**\nmonitor influenza antiviral supplies throughout the country and publicly report challenges in availability in any region, State, county, or metropolitan area; and\n**(2)**\nestablish a process, to be used in the case of a pandemic or during times when influenza antiviral supply availability is challenged, to ensure rapid and effective distribution of products to areas of urgent need in close coordination with manufacturers, distributors, and State and local health officials.\n##### (j) Plan for ensuring access to appropriate influenza therapeutics, preexposure prophylaxis, and diagnostics\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services shall publish a plan for ensuring access to appropriate influenza therapeutics, preexposure prophylaxis influenza antibody products, and influenza diagnostics, including during times when availability is challenged in certain regions or localities, for\u2014\n**(A)**\nhigh-risk patients, such as nursing home and pediatric patients;\n**(B)**\nhigh-exposure patients, such as first responders and health care workers; and\n**(C)**\nlow-income individuals, individuals covered by Medicaid, uninsured individuals, Tribal communities, and other underserved populations.\n**(2) Communications efforts**\nThe plan required by paragraph (1) shall include communications efforts to educate the public about the benefits of early use of influenza diagnostics, therapeutics, and preexposure prophylaxis products.\n#### 6. Authorizing sustainable funding for the influenza ecosystem\n##### (a) Influenza Planning and Response Program\nThere is authorized to be appropriated $231,358,000 for fiscal year 2027 and each subsequent fiscal year for programs and activities of the Centers for Disease Control and Prevention relating to influenza planning and response.\n##### (b) Strategic National Stockpile\nThere is authorized to be appropriated $1,000,000,000 for fiscal year 2027 and each subsequent fiscal year for the Strategic National Stockpile under section 319F\u20132 of the Public Health Service Act ( 42 U.S.C. 247d\u20136b ).\n##### (c) Industrial base management and supply chain\nThere is authorized $10,00,0000 for fiscal year 2027 and each subsequent fiscal year for the Center for Industrial Base Management and Supply Chain of the Administration for Strategic Preparedness and Response.\n##### (d) Hospital Preparedness Program\nThere is authorized to be appropriated $307,000,000 for fiscal year 2027 and each subsequent fiscal year for the Hospital Preparedness Program of the Administration for Strategic Preparedness and Response.\n##### (e) Universal Flu Vaccine Research\nThere is authorized to be appropriated $270,000,000 for fiscal year 2027 and each subsequent fiscal year for research of the National Institutes of Health to develop a universal flu vaccine.\n##### (f) Immunization Program\nThere is authorized to be appropriated $681,933,000 for fiscal year 2027 and each subsequent fiscal year for the immunization program of the Centers for Disease Control and Prevention under section 317 of the Public Health Service Act ( 42 U.S.C. 247b ).\n##### (g) Public Health Emergency Preparedness Program\nThere is authorized to be appropriated $735,000,000 for fiscal year 2027 and each subsequent fiscal year for the Public Health Emergency Preparedness Program of the Centers for Disease Control and Prevention.\n##### (h) Data Modernization Initiative\nThere is authorized to be appropriated $185,000,000 for fiscal year 2027 and each subsequent fiscal year for the Public Health Data Modernization Initiative of the Centers for Disease Control and Prevention.\n##### (i) Advanced Molecular Detection Program\nThere is authorized to be appropriated $43,000,000 for fiscal year 2027 and each subsequent fiscal year for the Advanced Molecular Detection Program at the Centers for Disease Control and Prevention.\n##### (j) Health defense operations budget matters\n**(1) Designation**\nSection 251(b)(2) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 901(b)(2) ) is amended by adding at the end the following:\n(H) Health defense operations (i) If, for any fiscal year, appropriations for discretionary accounts are enacted that the Congress designates in statute on an account-by-account basis as being for health defense operations, then the adjustment for that fiscal year shall be the total of such appropriations for that fiscal year. (ii) Any report or explanatory statement accompanying an appropriations Act that contains an account with amounts that are designated as being for health defense operations pursuant to clause (i) shall specify each program, project, or activity that will be funded by such amounts, and a specific dollar amount provided for each such program, project, or activity. .\n**(2) Professional bypass budget**\nTitle IV of the Public Health Service Act ( 42 U.S.C. 281 et seq. ) is amended by inserting after section 402B the following:\n402C. Health defense operations professional bypass budget (a) In general For fiscal year 2028 and each fiscal year thereafter, the Director of the Centers for Disease Control and Prevention, the Director of the National Institutes of Health, and the Assistant Secretary for Preparedness and Response shall prepare and submit directly to the President for review and transmittal to Congress, after reasonable opportunity for comment, but without change, by the Secretary of Health and Human Services, an annual budget estimate (including an estimate of the number and type of personnel needs for the Institutes) for amounts to be designated as being for health defense operations pursuant to subparagraph (H) of section 251(b)(2) of the Balanced Budget and Emergency Deficit Control Act of 1985. (b) Programs, projects, and activities Any budget estimate submitted pursuant to subsection (a) by the Director shall include any program, project, or activity that received funds designated under such subparagraph (H) for the fiscal year during which such budget is submitted, except that the Director may modify the programs, projects, or activities contained in such budget estimate as circumstances warrant. .",
      "versionDate": "2026-04-22",
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
        "name": "Health",
        "updateDate": "2026-05-21T16:31:14Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8447ih.xml"
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
      "title": "Protecting America from Seasonal and Pandemic Influenza Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting America from Seasonal and Pandemic Influenza Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect against seasonal and pandemic influenza, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:48Z"
    }
  ]
}
```
